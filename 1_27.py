def solution1(arr1, arr2):
    answer = [[]]
    i = 0
    for x in range(0, len(arr1)):
        try:
            x = int(arr1[i][0]) + int(arr2[i][0])
            del arr1[i][0]
            del arr2[i][0]
            print(arr1)
            answer[i].append(x)  # 이것때문에 오류가 생기는 것 같기도
            print(answer)       # answer.append(x) 하면 [[], 4] 형태로 나옴
            continue
        except:
            # arr1[i+1][0]에 대한 고민
            break
    return answer


def solution2(arr1, arr2):
    answer = []
    i = 0
    while i <= len(arr1)-1:
        list = []
        for x in range(0, len(arr1[i])):
            y = int(arr1[i][x]) + int(arr2[i][x])
            list.append(y)
        answer.append(list)
        i += 1
    return answer


print(solution2([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
