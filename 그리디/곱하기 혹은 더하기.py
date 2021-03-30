s = input()
n = list(map(int, s))

total = n[0]
for i in range(1, len(s)):
  if n[i - 1] <= 1:
    total += n[i]
  else:
    total *= n[i]

print(total)