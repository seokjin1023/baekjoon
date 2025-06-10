import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    length = sorted([a, b, c])
    if length[2] >= length[0] + length[1]:
        print("wrong")
    else:
        if length[2]**2 == length[0]**2 + length[1]**2:
            print("right")
        else:
            print("wrong")