# Graph

- [Graph](#graph)
  - [1. Assigned 📌](#1-assigned-)
    - [ACMIC homework Link 👨‍💻](#acmic-homework-link-)
  - [2. Free 🤗](#2-free-)
    - [All of Graph Problems 👩‍💻](#all-of-graph-problems-)
  - [3. Algorithms](#3-algorithms)
  - [4. Tree 순회](#4-tree-순회)


## 1. Assigned 📌
### [ACMIC homework Link 👨‍💻](https://www.acmicpc.net/group/practice/9719/2)
|name|solution|key words|
|:-:|:-:|:-:|
|[The Great Revegetation (Silver)](https://www.acmicpc.net/problem/17038)|||
|[Cycle Detection](https://www.acmicpc.net/problem/7097)|||
|[촌수계산](https://www.acmicpc.net/problem/2644)|||
|[Count Circle Groups](https://www.acmicpc.net/problem/10216)|||
|[부등호](https://www.acmicpc.net/problem/2529)|||

## 2. Free 🤗
### [All of Graph Problems 👩‍💻](https://www.acmicpc.net/problemset?sort=ac_desc&algo=7)

자유롭게 풀고 풀이를 올린 문제

|name|solution|key words|info|
|:-:|:-:|:-:|:--|
|섬의개수|[Solved by Bumjin](problems/섬의개수)|bfs |bfs 기본 문제, max recursion을 setting 해야 풀 수 있음. |
|이진 검색 트리|[Solved by Bumjin](problems/이진검색트리)|트리, 전위, 후위 순회|트리를 만들지 않고도 풀 수 있다. 하지만 나는 트리를 만들어서 풀었다.|

## 3. Algorithms 

* [이미지 출저 및 설명](https://towardsdatascience.com/10-graph-algorithms-visually-explained-e57faa1336f3)

|**BFS(Breath First Search)**|**DFS(Depth First Search)**|
|---|---|
|<img src="https://miro.medium.com/max/500/1*fYKrGW0IUeoS_8XtCoNaLw.gif" width=200px>|<img src="https://miro.medium.com/max/500/1*Ehes66L2dLrySl9K965Gjw.gif" width=200px>|

|**Minimal Spanning Tree**|**Shortest Path**|**Cycle Detection**|
|:-:|:-:|:-:|
|<img src="https://miro.medium.com/max/500/1*pdvKVRayHXNAyb64J2QwhA.gif" width=200px>|<img src="https://miro.medium.com/max/500/1*OUqMXd2jmLprCqWULLll8w.gif" width=200px>|<img src="https://miro.medium.com/max/500/1*ScXYdVPDFG1jP1GwiEBkWQ.gif" width=200px>|
|[Prim’s algorithm](algorithms/Prim) </br> [Kruskal’s algorithm](algorithms/Kruskal)|[Dijkstra’s shortest path algorithm](algorithms/DijkstraShortestPath)</br> [Bellman–Ford algorithm](algorithms/Bellman–Ford)|[Floyd cycle detection algorithm](algorithms/Floyd%20cycle%20detection%20algorithm)</br> [Brent’s algorithm](algorithms/Brent’s%20algorithm)|


|**Strongly Connected Components**|**Topological Sorting**|**Graph Colouring**
|:-:|:-:|:-:|
|<img src="https://miro.medium.com/max/500/1*mW2CO2dhTkvgsJK7oSrFJg.gif" width=200px>|<img src="https://miro.medium.com/max/500/1*tdDEOGGAn-L6MpdxDlaJkw.gif" width=200px>|<img src="https://miro.medium.com/max/500/1*SSSa5VrhhjNrXDdWTBGXlA.gif" width=200px>|
|[Kosaraju’s algorithm](algorithms/Kosaraju)</br>[Tarjan](algorithms/Tarjan’s%20strongly%20connected%20components)| [Kahn’s algorithm](algorithms/Kahn) </br> [based on depth-first search](algorithms/Topological_dfs)|[Algorithms using BFS or DFS](algorithms/graph_colouring_bfs_dfs) </br> [Greedy colouring](algorithms/Greedycolouring) |


## 4. Tree 순회

<kbd>
<img src="docs/traversal.png" width=800px>
</kbd>

|PreOrder|InOrder|PostOrder|
|:-:|:-:|:-:|
|**Node**-Left-Right|Left-**Node**-Right|Left-Right-**Node**|