def solution(n):
    answer = 0

    if not 0 <= n <= 3000:
        return False
    else:
        for i in range(1, n+1):
            if n % i == 0:
                answer += i

    return answer


print(solution(12))
print(solution(10))
