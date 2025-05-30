import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

answer = 0
#1자
value = 0
for i in range(n):
    value = arr[i][0] + arr[i][1] + arr[i][2] + arr[i][3]
    answer = max(answer, value)
    for j in range(1, m - 3):
        value = value - arr[i][j - 1] + arr[i][j + 3]
        answer = max(answer, value)
for i in range(m):
    value = arr[0][i] + arr[1][i] + arr[2][i] + arr[3][i]
    answer = max(answer, value)
    for j in range(1, n - 3):
        value = value - arr[j - 1][i] + arr[j + 3][i]
        answer = max(answer, value)
#나머지
out = [[0, 1, 2, 3], [0, 1, 2, 5], [0, 3, 4, 5], [2, 3, 4, 5], [0, 1, 3, 4], [1, 2, 4, 5], [1, 2, 3, 4], [0, 1, 4, 5], [0, 1, 2, 4], [1, 3, 4, 5]]
for i in range(n - 1):
    for j in range(m - 2):
        for a, b, c, d in out:
            value = arr[i + a // 3][j + a % 3] + arr[i + b // 3][j + b % 3]
            value += arr[i + c // 3][j + c % 3]
            value += arr[i + d // 3][j + d % 3]
            answer = max(answer, value)
out = [[0, 1, 3, 5], [0, 1, 2, 4], [1, 3, 4, 5], [0, 2, 4, 5], [0, 1, 2, 3], [2, 3, 4, 5], [0, 2, 3, 5], [1, 2, 3, 4], [0, 2, 3, 4], [1, 2, 3, 5]]
for i in range(n - 2):
    for j in range(m - 1):
        for a, b, c, d in out:
            value = arr[i + a // 2][j + a % 2] + arr[i + b // 2][j + b % 2]
            value += arr[i + c // 2][j + c % 2]
            value += arr[i + d // 2][j + d % 2]
            answer = max(answer, value)
print(answer)