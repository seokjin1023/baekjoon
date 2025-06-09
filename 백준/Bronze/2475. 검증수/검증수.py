import sys

input = sys.stdin.readline

num = list(map(int, input().split()))
print(sum(n * n for n in num) % 10)