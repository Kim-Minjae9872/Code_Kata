def solution(arr):
    answer = []
    for i, x in enumerate(arr):
        if x == min(arr):
            arr.pop(i)
            if arr == []:
                answer.append(-1)
            else:
                answer = arr
    return answer


def solution(arr):
    answer = []
    for x in arr:
        if x == min(arr):
            pass
        else:
            answer.append(x)
    if answer == []:
        answer.append(-1)
    return answer

# 위의 코드 둘다 시간초과로 실패


def solution(arr):
    answer = []
    x = min(arr)
    if len(arr) <= 1:
        answer.append(-1)
        return answer
    else:
        arr.remove(x)
        answer = arr
        return answer

# remove 함수가 생각이 안났다. (리스트 요소 빼기로 검색해서 찾음)


print(solution([4, 3, 2, 1]))
print(solution([10]))
print(solution([-555, 100, 245326809, 243]))
