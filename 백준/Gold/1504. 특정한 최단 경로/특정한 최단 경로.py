import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N, E = map(int, input().split())
edge = defaultdict(list)
for i in range(E):
    a, b, weight = map(int, input().split())
    edge[a].append([b, weight])
    edge[b].append([a, weight])

v1, v2 = map(int, input().split())

def get_min_distance(start) -> list:
    pq = []
    distance = [float('inf')] * (N + 1)
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    while pq:
        curW, curV = heapq.heappop(pq)
        if distance[curV] < curW:
            continue

        distance[curV] = curW

        for e in edge[curV]:
            if distance[e[0]] > distance[curV] + e[1]:
                distance[e[0]] = distance[curV] + e[1]
                heapq.heappush(pq, (distance[e[0]], e[0]))
    return distance
min_distance = float('inf')
start_from_1 = get_min_distance(1)
start_from_v1 = get_min_distance(v1)
start_from_v2 = get_min_distance(v2)
if start_from_1[v1] != float('inf') and start_from_v1[v2] != float('inf') and start_from_v2[N] != float('inf'):
    min_distance = min(min_distance, start_from_1[v1] + start_from_v1[v2] + start_from_v2[N])
if start_from_1[v2] != float('inf') and start_from_v2[v1] != float('inf') and start_from_v1[N] != float('inf'):
    min_distance = min(min_distance, start_from_1[v2] + start_from_v2[v1] + start_from_v1[N])

if min_distance == float('inf'):
    print(-1)
else:
    print(min_distance)