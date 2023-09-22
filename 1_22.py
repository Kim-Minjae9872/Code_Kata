def solution(a, b):
    answer = 0
    # n = len(a)
    # for x in range(0, n):
    for x in range(0, len(a)):
        answer += a[x]*b[x]

    return answer


print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))
print(solution([-1, 0, 1], [1, 0, -1]))
print(solution([-12, 0, 36], [2, 5, 4]))
