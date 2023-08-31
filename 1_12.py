# def solution(a, b):        오류 발생(아마 마이너스 값일때 오류가 생기는듯)

#     if a == b:
#         return a or b
#     elif a > b:
#         return sum([ax for ax in range(a+1)]) - sum([bx for bx in range(b)])
#     else:
#         return sum([bx for bx in range(b+1)]) - sum([ax for ax in range(a)])

def solution(a, b):
    answer = 0
    while True:
        if a == b:
            answer = answer + a
            break

        elif a < b:
            answer = answer + a
            a = a+1
            continue
        elif a > b:
            answer = answer + b
            b = b+1
            continue

    return answer


print(solution(0, 3))
print(solution(-1, -5))
print(solution(-3, 3))
