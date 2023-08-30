def solution(n):
    x = range(1, n+1)
    for i in x:
        if i**2 == n:
            return (i+1)**2
# 여기까지 구현하고 이후 해당하지 않는 값을 -1로 뽑아내는데에서 막힘, 해당하지 않는 값이 None인것을 확인

    return -1  # 내부에서 조건을 잡아줄 필요 없이 값이 없는 친구는 for문 밖에서 -1만 return하도록


print(solution(121))
print(solution(244))
print(solution(36))
