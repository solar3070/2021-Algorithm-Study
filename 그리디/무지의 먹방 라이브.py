def solution(food_times, k):
    answer = 0

    n = len(food_times)
    while k != -1:
        for i in range(n):
            answer = i
            if k == -1:
                break
            if food_times[i] > 0:
                k -= 1 
                food_times[i] -= 1
        if sum(food_times) == 0:
            answer = -1
            break

    return answer

food_times = list(map(int, input().split()))
k = int(input())

print(solution(food_times, k))