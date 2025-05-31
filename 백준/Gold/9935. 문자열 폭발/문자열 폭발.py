import sys
input = sys.stdin.readline

original = list(input().rstrip())
bomb = list(input().rstrip())
cut = len(bomb)

answer = []
for char in original:
    answer.append(char)
    if len(answer) >= cut:
        if answer[-cut:] == bomb:
            del answer[-cut:]

if not answer:
    print("FRULA")
else:
    print(''.join(answer))
