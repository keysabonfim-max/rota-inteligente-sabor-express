# Roteiro do vídeo pitch — até 4 minutos

## 1. Introdução — 30 segundos

Olá, neste projeto desenvolvemos uma solução chamada Rota Inteligente para a empresa fictícia Sabor Express.

O problema identificado é a dificuldade de organizar entregas nos horários de pico. Rotas definidas manualmente podem aumentar a distância percorrida, o tempo de entrega e os custos operacionais.

## 2. Solução — 50 segundos

A nossa proposta representa a região como um grafo. Os pontos representam locais de entrega e as ligações representam ruas com custos associados à distância.

Para encontrar caminhos eficientes utilizamos o algoritmo A*, que combina o custo já percorrido com uma estimativa do custo restante.

Também utilizamos K-Means para agrupar entregas próximas em diferentes zonas.

## 3. Demonstração — 1 minuto e 30 segundos

Neste momento, mostrar o arquivo `src/main.py`.

Primeiro, o programa carrega os dados das entregas.

Depois, o K-Means agrupa os pedidos de acordo com suas coordenadas.

Em seguida, o A* calcula os caminhos entre os pontos da rota.

O programa compara uma rota de referência com a rota otimizada e calcula a redução percentual da distância.

Por fim, é gerado um gráfico mostrando o mapa, os pontos de entrega, os grupos e a rota.

## 4. Resultados — 40 segundos

Os resultados são apresentados automaticamente no terminal. A solução permite visualizar a diferença entre a rota de referência e a rota otimizada.

Como os dados são simulados, os resultados representam um cenário acadêmico e servem para demonstrar a aplicação dos conceitos de Inteligência Artificial.

## 5. Conclusão — 30 segundos

Como conclusão, o projeto mostra que algoritmos de busca em grafos e técnicas de clustering podem ser utilizados conjuntamente para apoiar problemas de logística.

Como melhorias futuras, seria possível integrar mapas reais, trânsito em tempo real, horários de entrega e capacidade dos veículos.

Obrigado!
