def count(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    return cnt


def solution(left, right):
    answer = 0
    for x in range(left, right+1):
        if count(x) % 2 == 0:
            answer += x
        else:
            answer -= x

    return answer


print(solution(13, 17))
print(solution(24, 27))
print(solution(12, 33))
