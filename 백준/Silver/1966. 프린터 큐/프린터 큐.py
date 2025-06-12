import sys
from collections import deque

input = sys.stdin.readline

def high_pri(priority):
    for i in range(9, 0, -1):
        if priority[i] > 0:
            return i

T = int(input())
for _ in range(T):
    priority = [0] * 10
    N, find = map(int, input().split())
    sheet_pri = list(map(int, input().split()))
    sheet = deque()
    for i in range(N):
        sheet.append((i, sheet_pri[i]))
        priority[sheet_pri[i]] += 1
    answer = 1
    high = high_pri(priority)
    while True:
        count, pri = sheet.popleft()
        if pri == high:
            if count == find:
                print(answer)
                break
            else:
                answer += 1
                priority[pri] -= 1
                high = high_pri(priority)
        else:
            sheet.append((count, pri))