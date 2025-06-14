import sys
import math

input = sys.stdin.readline

N = int(input())
dp = [10] * (N + 1)
square = []
for i in range(1, 225):
    square.append(i * i)
for i in range(1, N + 1):
    if float(math.sqrt(i)).is_integer():
        dp[i] = 1
    else:
        for num in square:
            if num >= i:
                break
            dp[i] = min(dp[i], dp[num] + dp[i - num])
print(dp[N])