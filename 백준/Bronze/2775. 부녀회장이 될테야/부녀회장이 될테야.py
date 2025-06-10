import sys

input = sys.stdin.readline

T = int(input())
dp = [[0] * 15 for _ in range(15)]
for _ in range(T):
    k = int(input())
    n = int(input())
    num = [i + 1 for i in range(n)]
    for _ in range(k):
        for i in range(1, n):
            num[i] += num[i - 1]
    print(num[n - 1])