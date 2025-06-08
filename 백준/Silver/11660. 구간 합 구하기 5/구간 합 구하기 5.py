import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))
for i in range(n):
    for j in range(1, n):
        nums[i][j] += nums[i][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    if x1 == x2:
        if y1 == 0:
            print(nums[x1][y2])
        else:
            print(nums[x2][y2] - nums[x1][y1 - 1])
    else:
        answer = 0
        for i in range(x1, x2 + 1):
            if y1 == 0:
                answer += nums[i][y2]
            else:
                answer += nums[i][y2] - nums[i][y1 - 1]
        print(answer)