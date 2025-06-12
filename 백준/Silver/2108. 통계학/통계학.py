import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
value = [int(input()) for _ in range(N)]
print(round(sum(value) / N))
value.sort()
print(value[N // 2])
#최빈값
counter = Counter(value)
max_count = max(counter.values())
indices = [value for value, count in counter.items() if count == max_count]
indices.sort()
if len(indices) == 1:
    print(indices[0])
else:
    print(indices[1])
print(value[len(value) - 1] - value[0])