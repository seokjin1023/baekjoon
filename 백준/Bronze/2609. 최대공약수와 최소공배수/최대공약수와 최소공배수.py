import sys

input = sys.stdin.readline

def gcd(a, b):
    while True:
        if a % b == 0 or b % a == 0:
            break
        if a > b:
            a %= b
        else:
            b %= a

    if a % b == 0:
        return b
    elif b % a == 0:
        return a

def lcm(a, b):
    return a * b // gcd(a, b)

a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))