def solution(s):
    answer = True
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if len(s) == 4 or len(s) == 6:
        for x in s:
            if x in str(num):
                pass
            else:
                answer = False
    else:
        answer = False
    return answer


print(solution("a234"))
print(solution("1234"))
print(solution("46921825623"))
