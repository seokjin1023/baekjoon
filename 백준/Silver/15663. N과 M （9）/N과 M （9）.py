import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))
seq.sort()
result = sorted(set(permutations(seq, m)))
for sequence in result:
    print(*sequence)
