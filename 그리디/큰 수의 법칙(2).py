# 풀이보고 다시 풀기

n, m, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
first = num[n - 1]
second = num[n - 2]

# 수열
sum = first * k + second
# 수열이 반복될 수 있는 만큼 + 수열이 잘릴 때 
result = m // (k + 1) * sum + m % (k + 1) * first

print(result)