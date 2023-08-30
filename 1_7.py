# def solution(n):
#     answer = []

#     for x in str(n):
#         answer.append(int(x))
#     answer.sort(reverse=True)
#     return answer                샘플은 통과했으나 제출 시 테스트 실패


def solution(n):
    answer = []

    for x in str(n):
        answer.append(int(x))
    answer.reverse()
    return answer                #오름차순이 아닌 단순 반대로 배열


print(solution(12345))
print(solution(4560890))
