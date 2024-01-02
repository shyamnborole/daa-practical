from math import inf as INF

graph = [    [0, 3, INF, 7],
             [8, 0, 2, INF],
             [5, INF, 0, 1],
             [2, INF, INF, 0]
        ]

V=4
print("Original graph:")
print(graph)
for k in range(V):
        for i in range(V):
            for j in range(V):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

print("Graph after applying Floyd-Warshall algorithm:")
print(graph)