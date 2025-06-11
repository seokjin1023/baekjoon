import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
card = [i for i in range(1, N + 1)]
card = deque(card)
while True:
    if len(card) == 1:
        print(card[0])
        break

    card.popleft()
    card.append(card.popleft())