def solution(absolutes, signs):
    answer = 0
    for i, x in enumerate(signs):
        if x == True:
            answer = answer + absolutes[i]
        else:
            answer = answer - absolutes[i]

    return answer


print(solution([4, 7, 12], [True, False, True]))
print(solution([1, 2, 3], [False, False, True]))
