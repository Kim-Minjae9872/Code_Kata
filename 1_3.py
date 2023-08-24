def solution(n):
    answer = 0

    if not 0 < n < 100000000:
        return False
    else:
        for x in str(n):
            answer += int(x)
        return answer


print(solution(-125))
print(solution(987))
print(solution(123456))
