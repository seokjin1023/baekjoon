import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())
answer = 0
while n > 0:
    if r >= 2**(n-1):
        if c >= 2**(n-1):
            answer += 3*(2**(n-1) * 2**(n-1))
        else:
            answer += 2*(2**(n-1) * 2**(n-1))
    else:
        if c >= 2**(n-1):
            answer += 2**(n-1) * 2**(n-1)
    r = r % (2**(n-1))
    c = c % (2**(n-1))
    n -= 1
print(answer)

