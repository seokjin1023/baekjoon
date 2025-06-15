import sys
import re
from collections import deque

input = sys.stdin.readline

line = input().rstrip()
value = re.split(r'([+-])', line)
answer = []
count_minus = 0
result = 0
for val in value:
    if val.isdigit():
        result += int(val)
    else:
        if val == '-':
            count_minus += 1
            answer.append(result)
            result = 0
answer.append(result)
if count_minus == 0:
    print(answer[0])
else:
    ans = answer[0]
    for i in range(1, len(answer)):
        ans -= answer[i]
    print(ans)