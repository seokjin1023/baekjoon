import sys

input = sys.stdin.readline

N = int(input())
if N == 0:
    print("NO")
    exit(0)
fact = [1]
for i in range(1, 22):
    fact.append(fact[i - 1] * i)
for val in reversed(fact):
    if N >= val:
        N -= val
print("YES" if N == 0 else "NO")