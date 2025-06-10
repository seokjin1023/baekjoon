import sys

input = sys.stdin.readline

isbn = input().strip()
missing_idx = -1
total = 0

for i in range(13):
    if isbn[i] == '*':
        missing_idx = i
        continue

    digit = int(isbn[i])
    weight = 1 if i % 2 == 0 else 3
    total += digit * weight

weight = 1 if missing_idx % 2 == 0 else 3
for x in range(10):
    if (total + x * weight) % 10 == 0:
        print(x)
        break