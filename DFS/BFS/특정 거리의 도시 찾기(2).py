from collections import deque
import sys

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

dst = [0] * (n + 1)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                dst[i] = dst[v] + 1


visited = [False] * (n + 1)
bfs(graph, x, visited)

if k not in dst:
    print(-1)
else:
    for i, value in enumerate(dst):
        if value == k:
            print(i)