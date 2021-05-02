n, m = map(int, input().split())

graph = []
for _ in range (n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    result = 1
    while x != n - 1 or y != m - 1:
        if x + 1 <= n - 1 and graph[x + 1][y] == 1:     
            x += 1
        elif y + 1 <= m - 1 and graph[x][y + 1] == 1:
            y += 1
        result += 1
        graph[x][y] = result
    return result

print(bfs(0, 0))