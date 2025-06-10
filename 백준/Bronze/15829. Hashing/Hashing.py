import sys

input = sys.stdin.readline

r = 1
M = 1234567891
L = int(input())
string = input().rstrip()
answer = 0
for c in string:
    value = ord(c) - ord('a') + 1
    answer += r * value
    answer %= M
    r *= 31
    r %= M
print(answer)