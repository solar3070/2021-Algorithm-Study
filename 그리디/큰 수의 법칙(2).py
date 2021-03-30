n, m, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
first = num[n - 1]
second = num[n - 2]

# 수열(첫 번째 큰 수 * k + 두 번째 큰 수)
sum = first * k + second
# 수열이 반복될 수 있는 만큼 + 수열이 잘리는 경우
result = m // (k + 1) * sum + m % (k + 1) * first

print(result)