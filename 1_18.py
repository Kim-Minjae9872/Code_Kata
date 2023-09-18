def solution(numbers):
    ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    answer = 0
    for x in ls:
        if x in numbers:
            pass
        else:
            answer += x
    return answer


print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
print(solution([5, 8, 4, 0, 6, 7, 9]))
