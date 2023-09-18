def solution(phone_number):
    answer = ''
    rev = reversed(phone_number)
    for i, x in enumerate(list(rev)):
        if i == 0 or i == 1 or i == 2 or i == 3:
            # 개인 프로젝트때도 겪었던 if문에서의 or 사용 주의
            answer += x
        else:
            x = '*'
            answer += x
    return reversed(answer)
    # reversed(answer)은 <reversed object at 0x000001FF93CBAD60> 형태로 표현


def solution(phone_number):
    a = '*'*(phone_number.count('')-5)
    b = phone_number[-4:]
    return a+b


print(solution("01033334444"))
print(solution("027778888"))
