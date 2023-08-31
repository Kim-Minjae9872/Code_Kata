def solution(n):

    list = []

    for x in str(n):
        list.append(x)
    list.sort(reverse=True)
    answer = ''.join(list)
    return int(answer)


print(solution(118372))
print(solution(232159012))
