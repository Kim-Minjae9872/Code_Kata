def solution(n):
    list = []
    answer = 0
    for x in range(1, n+1):
        if n % x == 1:
            list.append(x)
            answer = min(list)
    return answer


print(solution(10))
print(solution(25))
print(solution(1415))
