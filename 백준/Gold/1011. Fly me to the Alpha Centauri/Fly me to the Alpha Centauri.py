import sys
input = sys.stdin.readline

T = int(input())
while T > 0:
    T -= 1
    x, y = map(int, input().split())
    distance = y - x
    i = 1
    while True:
        if i * i <= distance < (i + 1) * (i + 1):
            break
        i += 1
    if distance == i * i:
        print(2 * i - 1)
    else:
        if distance - i * i <= i:
            print(2 * i)
        else:
            print(2 * i + 1)


