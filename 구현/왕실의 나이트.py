location = input()

col = location[0]
row = location[1]

count = 8

if col == 'a' or col == 'h':
    count -= 3
elif col == 'b' or col == 'g':
    count -= 2

if row == '1' or row == '8':
    count -= 3
elif row == '2' or row == '7':
    count -= 2

print(count)