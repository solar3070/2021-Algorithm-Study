n, m = map(int, input().split())

data = []

import sys
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

temp = [[0] * m for _ in range(n)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바이러스 전염
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i] 

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# 안전 영역 크기
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 벽 설치, 최대 안전 영역 구하기
result = 0
def dfs(count):
    global result
    # 울타리 3개 
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 바이러스 전파
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 최대 안전 영역
        result = max(result, get_score())
        return
    # 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                count += 1
                data[i][j] = 1
                dfs(count)
                count -= 1
                data[i][j] -= 1

dfs(0)
print(result)