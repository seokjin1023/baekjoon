import sys
input = sys.stdin.readline

N = int(input())
color = [list(map(int, input().split())) for _ in range(N)]

blue = 0
white = 0
is_blue = True

def count_color(i, j, n):
    global blue, white, is_blue
    count = 0
    if color[i][j] == 0:
        is_blue = False
    else:
        is_blue = True
    for a in range(i, i + n):
        for b in range(j, j + n):
            if is_blue and color[a][b] == 1:
                count += 1
            elif not is_blue and color[a][b] == 0:
                count += 1
    if count == n * n:
        if is_blue:
            blue += 1
        else:
            white += 1
    else:
        count_color(i, j, n // 2)
        count_color(i + n //2, j, n // 2)
        count_color(i, j + n // 2, n // 2)
        count_color(i + n // 2, j + n // 2, n // 2)
count_color(0, 0, N)
print(white)
print(blue)
