n, m = map(int, input().split())

lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

city = sum(lst, [])


loc = city.index(2)
row = loc // n + 1
col = loc % n + 1




home = city.index(1)
home_row = loc // n + 1
home_col = loc % n + 1