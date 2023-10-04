def solution(price, money, count):
    total_price = 0
    for x in range(1, count+1):
        total_price += (price*x)
    if total_price - money >= 0:
        answer = total_price-money
        return answer
    else:
        answer = 0
        return answer


print(solution(3, 20, 4))
print(solution(3, 20, 2))
print(solution(15, 20, 2))
