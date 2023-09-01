def solution(num):
    answer = 0

    while True:
        if num % 2 == 0:
            num = num / 2
            answer += 1
            continue

        elif num == 1:
            break

        else:
            num = num*3 + 1
            answer += 1

    if answer >= 500:  # while 문을 돌면서 500번째가 되면 -1이 출력되게 하는게 best 아닐까?
        answer = -1

    return answer


print(solution(6))
print(solution(16))
print(solution(626331))
