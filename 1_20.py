def solution(s):
    answer = ''
    x = len(s)//2

    # if len(s) % 2 == 0:
    #     answer = s[len(s)/2]+s[len(s)/2+1]
    # string indices must be integers 오류

    if len(s) % 2 == 0:
        answer = s[x-1] + s[x]
    else:
        answer = s[x]

    return answer


print(solution('qwer'))
print(solution('abcde'))
print(solution('sadfdjslbozxuoiewqetcxzb'))
