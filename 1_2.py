def solution(arr):
    answer = 0
    if not 1 <= len(arr) <= 100:
        return False
    else:
        for x in arr:
            if not -10000 <= x <= 10000:
                return False
            else:
                answer += x / len(arr)
        return answer


print(solution([1, 2, 3, 4]))
print(solution([5, -11111]))
print(solution([-5, 5, 123, 341]))
