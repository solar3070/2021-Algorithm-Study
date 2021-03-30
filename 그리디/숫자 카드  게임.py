n, m = map(int, input().split())

cards = []
for _ in range(n):
  row = list(map(int, input().split()))
  cards.append(row)

minLst = []
for row in cards:
  minLst.append(min(row))

print(max(minLst))