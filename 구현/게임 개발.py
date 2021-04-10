n, m = map(int, input().split())
a, b, d = map(int, input().split())

gameMap = []
for _ in range(n):
    gameMap.append(list(map(int, input().split())))

count = 1
gameMap[a][b] = 2

while True:
    if d == 0: # 북쪽
        if gameMap[a][b - 1] == 0: # 가보지 않은 곳
            d = 1
            b -= 1
            gameMap[a][b] = 2
            count += 1
        else:
            d = 1
    elif d == 1:
        if gameMap[a + 1][b] == 0:
            d = 2
            a += 1
            gameMap[a][b] = 2
            count += 1
        else:
            d = 2
    elif d == 2:
        if gameMap[a][b + 1] == 0:
            d = 3
            b += 1
            gameMap[a][b] = 2
            count += 1
        else:
            d = 3
    elif d == 3:
        if gameMap[a - 1][b] == 0:
            d = 1
            a -= 1
            gameMap[a][b] = 2
            count += 1
        else:
            d = 1

    if gameMap[a][b - 1] and gameMap[a - 1][b] and gameMap[a + 1][b] and gameMap[a][b + 1]:
        if d == 0 and gameMap[a + 1][b] != 1:
            a += 1
        elif d == 1 and gameMap[a][b + 1] != 1:
            b += 1
        elif d == 2 and gameMap[a - 1][b] != 1:
            a -= 1
        elif d == 3 and gameMap[a][b - 1] != 1:
            b -= 1
        else:
            break

print(count)