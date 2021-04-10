# 못 푼 문제
n, m = map(int, input().split())
weight = list(map(int, input().split()))

# 무게마다 볼링공 개수
lst = [0] * 11
for i in weight:
    lst[i] += 1

result = 0
for i in range(1, m + 1):
    n -= lst[i] # 남은 공 개수
    result += lst[i] * n 

print(result)