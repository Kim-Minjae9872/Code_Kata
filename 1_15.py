def solution(arr, divisor):
    answer = []
    for x in arr:
        if x % divisor == 0:
            answer.append(x)

    if answer == []:
        answer.append(-1)
    return sorted(answer)


print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3, 2, 6], 10))
print(solution([33, 2, -1], 11))
