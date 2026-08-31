# Rota Inteligente: Otimização de Entregas com Algoritmos de IA

## 1. Descrição do problema

A Sabor Express é uma pequena empresa local de delivery de alimentos que enfrenta dificuldades para organizar suas entregas nos horários de pico. Atualmente, as rotas são definidas manualmente, o que pode gerar percursos ineficientes, atrasos, aumento do consumo de combustível e insatisfação dos clientes.

O objetivo deste projeto é desenvolver uma solução computacional baseada em Inteligência Artificial para apoiar a definição de rotas mais eficientes e organizar pedidos próximos em grupos.

## 2. Objetivos

- Representar a região de atendimento como um grafo.
- Encontrar caminhos eficientes entre os pontos utilizando o algoritmo A*.
- Agrupar pedidos próximos utilizando K-Means.
- Comparar a distância de uma rota manual com uma rota otimizada.
- Apresentar os resultados de forma visual.

## 3. Abordagem adotada

A cidade é representada por um grafo. Os nós representam pontos de entrega e as arestas representam ruas. Cada aresta possui um peso associado à distância entre os pontos.

O algoritmo A* é utilizado para encontrar um caminho de menor custo entre dois pontos. Para os pedidos, o K-Means é utilizado para identificar grupos de entregas geograficamente próximas.

O projeto utiliza dados simulados para representar uma pequena região urbana. Essa escolha permite demonstrar os fundamentos dos algoritmos sem depender de serviços externos de mapas.

## 4. Algoritmos utilizados

### A*

O A* é um algoritmo de busca heurística. Para cada ponto, ele considera o custo já percorrido e uma estimativa do custo restante.

A função utilizada é:

`f(n) = g(n) + h(n)`

Onde:
- `g(n)` representa o custo do caminho desde a origem até o nó atual;
- `h(n)` representa a estimativa do custo até o destino;
- `f(n)` representa o custo total estimado.

Neste projeto, a distância euclidiana é utilizada como heurística.

### K-Means

O K-Means é um algoritmo de aprendizado não supervisionado utilizado para agrupamento. Neste projeto, ele organiza os pedidos em zonas de entrega de acordo com a proximidade geográfica.

## 5. Estrutura do projeto

```text
rota-inteligente/
├── README.md
├── requirements.txt
├── data/
│   └── entregas.csv
├── docs/
│   └── grafo.png
└── src/
    └── main.py
```

## 6. Como executar

### Pré-requisitos

- Python 3.10 ou superior
- pip

### Instalação

```bash
pip install -r requirements.txt
```

### Execução

```bash
python src/main.py
```

O programa apresenta no terminal:
- grupos de entregas;
- caminhos encontrados pelo A*;
- distância total;
- comparação entre rota manual e rota otimizada.

Também gera uma imagem do grafo em `docs/grafo.png`.

## 7. Resultados

O programa calcula uma rota manual de referência e uma rota otimizada entre os pontos definidos no conjunto de dados. A diferença percentual é calculada automaticamente:

`redução (%) = ((distância manual - distância otimizada) / distância manual) × 100`

Como os dados são simulados, os valores representam um cenário acadêmico e não uma operação real da Sabor Express.

## 8. Limitações

- O mapa utilizado é simulado.
- Não são utilizados dados de trânsito em tempo real.
- O algoritmo não considera acidentes, obras ou bloqueios temporários.
- A distância utilizada é uma aproximação.
- O K-Means depende da quantidade de grupos escolhida.

## 9. Melhorias futuras

- Integrar dados reais de mapas.
- Utilizar trânsito em tempo real.
- Considerar janelas de horário de entrega.
- Adicionar capacidade máxima dos veículos.
- Utilizar técnicas mais avançadas para o problema de múltiplas entregas.
- Recalcular as rotas dinamicamente quando houver novos pedidos.

## 10. Conclusão

A solução demonstra como conceitos de Inteligência Artificial podem ser aplicados a um problema cotidiano de logística. A combinação de representação por grafos, busca heurística com A* e agrupamento com K-Means permite organizar os pedidos e buscar caminhos mais eficientes.

O projeto atende ao desafio proposto ao demonstrar uma estratégia computacional para redução de percursos e organização das entregas, servindo como protótipo para uma solução que poderia ser expandida com dados reais.
