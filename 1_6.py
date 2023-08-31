# def solution(x, n):
#     answer = []
#     for i in range(x, x*(n+1), x):
#         answer.append(i)

#     return answer        런타임 에러

def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)

    return answer


print(solution(2, 5))
print(solution(1523, 25))
print(solution(-4, 2))



