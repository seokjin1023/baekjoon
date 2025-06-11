import sys

input = sys.stdin.readline

N = int(input())
s = list(map(int, input().split()))
s = set(s)
M = int(input())
find = list(map(int, input().split()))
for val in find:
    if val in s:
        print(1)
    else:
        print(0)