n = int(input())
count = 0

List = [500, 100, 50, 10]

for coin in List:
  if n // coin > 0:
    count += n // coin
    n %= coin

print(count)