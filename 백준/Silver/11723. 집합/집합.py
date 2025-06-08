import sys
from itertools import permutations

input = sys.stdin.readline

M = int(input())
s = set()
for _ in range(M):
    parts = input().split()
    instruction = parts[0]
    num = int(parts[1]) if len(parts) > 1 else None
    if instruction == 'add':
        s.add(num)
    elif instruction  == 'remove':
        s.discard(num)
    elif instruction == 'check':
        print(1 if num in s else 0)
    elif instruction == 'toggle':
        s.symmetric_difference_update({num})
    elif instruction == 'all':
        for i in range(1, 21):
            s.add(i)
    elif instruction == 'empty':
        s.clear()