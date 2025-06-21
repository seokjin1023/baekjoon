def solution(storey):
    answer = 0
    while storey > 0:
        last = storey % 10
        storey //= 10
        if last > 5:
            answer += 10 - last
            storey += 1
        else:
            if last == 5 and storey % 10 >= 5:
                answer += 10 - last
                storey += 1
            else:
                answer += last
    return answer