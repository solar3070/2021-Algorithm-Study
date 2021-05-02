n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dst1 = graph[x - 1] # 2, 3
lst = []
def dfs(k, x):
    dst = 0
    while dst < k
        for i in range dst1:
            dfs(k - 1, i) 




dfs(k, x)