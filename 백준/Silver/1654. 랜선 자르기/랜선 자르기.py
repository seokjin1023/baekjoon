import sys
import heapq
from collections import deque

input = sys.stdin.readline


K, N = map(int, input().split())
length = [int(input().rstrip()) for _ in range(K)]
length.sort()

def line_count(arr, size):
    count = 0
    for line in arr:
        count += line // size
    return count

start = 1
end = max(length)  
result = 0

while start <= end:
    mid = (start + end) // 2
    cut = line_count(length, mid)

    if cut >= N:
        result = mid 
        start = mid + 1
    else:
        end = mid - 1

print(result)