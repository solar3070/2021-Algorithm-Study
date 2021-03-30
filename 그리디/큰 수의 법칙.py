# 첫 번째 풀기

n, m, k = map(int, input().split())
lst = list(map(int, input().split()))

maxNum = max(lst)
sum = 0
count = 0
temp = 0

while count < m:
  if maxNum >= temp: 
    for _ in range(k):
      sum += maxNum
      count += 1
      if count == m:
        break
  else:
    sum += maxNum
    count += 1 
  temp = maxNum
  lst.remove(maxNum)
  maxNum = max(lst)
  lst.append(temp)
  
print(sum)