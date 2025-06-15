import sys
import re
from collections import deque

input = sys.stdin.readline

N = int(input())
fruit = list(map(int, input().split()))
count = [0] * 10
i = 0
j = 0
count[fruit[0]] += 1
ans = 0
def count_fruit():
    kind = 0
    for i in range(10):
        if count[i] != 0:
            kind += 1
    return kind

while True:
    if count_fruit() > 2:
        while count_fruit() > 2:
            count[fruit[i]] -= 1
            i += 1
    ans = max(ans, j - i + 1)
    j += 1
    if j >= N:
        break
    count[fruit[j]] += 1
print(ans)