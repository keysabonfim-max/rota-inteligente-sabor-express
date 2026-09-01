import math
import heapq
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "entregas.csv"
OUTPUT_FILE = BASE_DIR / "docs" / "grafo.png"

NODES = {
    "A": (0, 0), "B": (2, 2), "C": (5, 2), "D": (1, 5),
    "E": (4, 5), "F": (7, 4), "G": (6, 0), "H": (9, 2)
}

EDGES = {
    "A": [("B", 2.83), ("D", 5.10)],
    "B": [("A", 2.83), ("C", 3.00), ("D", 3.16)],
    "C": [("B", 3.00), ("E", 3.16), ("G", 2.83)],
    "D": [("A", 5.10), ("B", 3.16), ("E", 3.00)],
    "E": [("D", 3.00), ("C", 3.16), ("F", 3.16)],
    "F": [("E", 3.16), ("G", 4.12), ("H", 2.83)],
    "G": [("C", 2.83), ("F", 4.12), ("H", 3.61)],
    "H": [("F", 2.83), ("G", 3.61)]
}

def heuristic(node, goal):
    x1, y1 = NODES[node]
    x2, y2 = NODES[goal]
    return math.hypot(x2 - x1, y2 - y1)

def a_star(start, goal):
    frontier = [(heuristic(start, goal), 0.0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0.0}

    while frontier:
        _, current_cost, current = heapq.heappop(frontier)

        if current == goal:
            break

        if current_cost > cost_so_far[current]:
            continue

        for neighbor, edge_cost in EDGES[current]:
            new_cost = current_cost + edge_cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(frontier, (priority, new_cost, neighbor))
                came_from[neighbor] = current

    if goal not in came_from:
        return [], float("inf")

    path, current = [], goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path, cost_so_far[goal]

def build_route(stops):
    full_path, total = [], 0.0
    for start, goal in zip(stops, stops[1:]):
        path, distance = a_star(start, goal)
        if not path:
            raise ValueError(f"Sem caminho entre {start} e {goal}.")
        full_path.extend(path if not full_path else path[1:])
        total += distance
    return full_path, total

def optimize_order(start, deliveries):
    """Escolhe a próxima entrega ainda não visitada pelo menor custo A*."""
    remaining = set(deliveries)
    route = [start]
    current = start
    total = 0.0

    while remaining:
        candidates = []
        for target in remaining:
            _, distance = a_star(current, target)
            candidates.append((distance, target))
        distance, target = min(candidates)
        route.append(target)
        total += distance
        current = target
        remaining.remove(target)

    return route, total

def cluster_deliveries(df, n_clusters=3):
    model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    result = df.copy()
    result["grupo"] = model.fit_predict(result[["x", "y"]])
    return result

def draw_graph(route, clustered):
    plt.figure(figsize=(10, 7))
    drawn = set()

    for node, neighbors in EDGES.items():
        x1, y1 = NODES[node]
        for neighbor, _ in neighbors:
            edge = tuple(sorted((node, neighbor)))
            if edge in drawn:
                continue
            x2, y2 = NODES[neighbor]
            plt.plot([x1, x2], [y1, y2], linewidth=1.5)
            drawn.add(edge)

    for node, (x, y) in NODES.items():
        plt.scatter(x, y, s=100)
        plt.text(x + 0.12, y + 0.12, node, fontsize=11)

    for grupo, grupo_df in clustered.groupby("grupo"):
        plt.scatter(
            grupo_df["x"], grupo_df["y"], s=160, alpha=0.55,
            label=f"Grupo {grupo + 1}"
        )

    coords = [NODES[n] for n in route]
    plt.plot(
        [p[0] for p in coords], [p[1] for p in coords],
        linewidth=3, marker="o", label="Rota otimizada"
    )

    plt.title("Sabor Express - Rota Inteligente")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.grid(True, alpha=0.25)
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_FILE, dpi=150)
    plt.close()

def main():
    df = pd.read_csv(DATA_FILE)
    clustered = cluster_deliveries(df, 3)

    delivery_nodes = df["local"].str.extract(r"([A-H])$")[0].tolist()

    # Cenário manual de referência, propositalmente pouco eficiente.
    manual_stops = ["A", "D", "B", "D", "E", "C", "G", "F", "H"]
    manual_route, manual_distance = build_route(manual_stops)

    # Estratégia automática: A* calcula cada trecho e a heurística
    # de escolha prioriza a entrega ainda não visitada mais próxima.
    optimized_stops, optimized_distance = optimize_order("A", delivery_nodes)
    optimized_route, _ = build_route(optimized_stops)

    reduction = ((manual_distance - optimized_distance) / manual_distance) * 100

    print("\n=== ROTA INTELIGENTE - SABOR EXPRESS ===")
    print("\nEntregas e grupos:")
    print(clustered[["pedido", "local", "x", "y", "grupo"]].to_string(index=False))

    print("\nRota manual de referência:")
    print(" -> ".join(manual_route))
    print(f"Distância: {manual_distance:.2f} unidades")

    print("\nOrdem otimizada das entregas:")
    print(" -> ".join(optimized_stops))
    print("\nCaminho calculado pelo A*:")
    print(" -> ".join(optimized_route))
    print(f"Distância: {optimized_distance:.2f} unidades")
    print(f"\nRedução estimada da distância: {reduction:.2f}%")

    draw_graph(optimized_route, clustered)
    print(f"\nGráfico salvo em: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
