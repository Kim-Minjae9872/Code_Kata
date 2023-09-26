def solution(s):
    answer = ''
    lis = []
    for x in s:
        lis.append(ord(x))
        lis = lis

    while len(lis):
        for x in lis:
            if x == max(lis):
                answer += chr(x)
                lis.remove(x)
                continue
    return answer


print(solution("Zbcdefg"))
print(solution("ZbcAebOFg"))
