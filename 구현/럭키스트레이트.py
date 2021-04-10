n = int(input())
length = len(str(n))
middle = length // 2

leftSum = rightSum = 0

for i in range(length):
    if i < middle:
        leftSum += int(str(n)[i])
    else:
        rightSum += int(str(n)[i])
    
if leftSum == rightSum:
    print("LUCKY")
else:
    print("READY")