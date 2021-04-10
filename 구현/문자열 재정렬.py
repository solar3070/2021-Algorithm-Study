s = input()

alpha_list = []
num = 0

for i in s:
    if i.isalpha():
        alpha_list += i
    else:
        num += int(i)

alpha_list.sort()
alpha = "".join(alpha_list)
print(alpha + str(num))