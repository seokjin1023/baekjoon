from collections import deque
def dfs(num, visited, computers):
    visited[num] = True
    for j in range(len(computers[num])):
        if computers[num][j] == 1 and not visited[j]:
            dfs(j, visited, computers)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    que = deque()
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, computers)
            answer += 1
    return answer