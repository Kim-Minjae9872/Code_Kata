def solution(n):
    answer = '수박' * (n//2)
    if n % 2 != 0:
        answer += '수'
    return answer


print(solution(3))
print(solution(6))
print(solution(132))
