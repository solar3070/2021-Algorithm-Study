s = input()
n = list(map(int, s))

count = [0, 0]

count[n[0]] += 1
for i in range(1, len(s)):
    if n[i - 1] != n[i]:
        count[n[i]] += 1

print(min(count))