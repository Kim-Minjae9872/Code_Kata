def solution(seoul):
    answer = ''
    for i, x in enumerate(seoul):
        if x == 'Kim':
            answer = f'김서방은 {i}에 있다'
    return answer


seoul = ["Jane", "Kim"]
busan = ["Lee", "Son", "Park", "Kim"]

print(solution(seoul))
print(solution(busan))
