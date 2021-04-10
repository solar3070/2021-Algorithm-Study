def solution(s):
    len_list = [len(s) + 1] * (len(s) + 1)
    for i in range(1, len(s) + 1):
        w = s[0:i]
        same = count = 1
        short = ""
        for j in range(i, len(s) + 1, i):
            if w != s[j:j + i]:
                same = 0

            if same == 0:
                if count == 1:
                    short += w
                else:
                    short += str(count) + w
                same = count = 1
            else:
                count += 1
            w = s[j:j + i]

            if j + i >= len(s):
                if j + i == len(s):
                    if count == 1:
                        short += w
                    else:
                        short += str(count) + w
                elif j + i > len(s):
                    short += s[j:]
                len_list[i] = len(short)
                break

    return min(len_list)

s = input()
print(solution(s))