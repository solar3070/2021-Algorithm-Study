import sys
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

lst = []

def dfs(k, x):
    if k == 0:
        lst.append(x);
        return

    dst1 = graph[x]
    for i in dst1:
        dfs(k - 1, i) 

dfs(k, x)

if k != 1:
    for i in lst:
        if i in graph[x]:
            lst.remove(i)

lst.sort()

if not lst: # 빈 리스트 확인
    print(-1)
else:
    for i in lst:
        print(i)