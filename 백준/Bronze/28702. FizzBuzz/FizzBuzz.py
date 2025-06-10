import sys

input = sys.stdin.readline

fiz = []
for _ in range(3):
    fiz.append(input().rstrip())

target = 0
for i in range(3):
    if fiz[i].isdigit():
        target = int(fiz[i]) + 3 - i
        break

if target % 3 == 0:
    if target % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
else:
    if target % 5 == 0:
        print("Buzz")
    else:
        print(target)