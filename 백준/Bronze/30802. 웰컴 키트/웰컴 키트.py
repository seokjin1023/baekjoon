import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
shirts = list(map(int, input().split()))
T, P = map(int, input().split())
answer = 0
for shirt in shirts:
    answer += shirt // T
    if shirt % T != 0:
        answer += 1
print(answer)
print("{} {}".format(N // P, N % P))