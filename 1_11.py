def solution(x):
    answer = True
    plus = 0

    for h in str(x):
        plus += int(h)
    if x % plus == 0:
        return answer
    else:
        return False


print(solution(18))
print(solution(11))
print(solution(13))
print(solution(111))
