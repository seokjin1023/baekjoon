import sys

class SegmentTree:
    def __init__(self, data):
        self.N = len(data)
        self.size = 1
        while self.size < self.N:
            self.size *= 2
        self.tree = [0] * (2 * self.size)
        for i in range(self.N):
            self.tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        index += self.size
        self.tree[index] = value
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]

    def query(self, left, right):
        left += self.size
        right += self.size
        result = 0
        while left <= right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 0:
                result += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return result

input = sys.stdin.readline

N, M, K = map(int, input().split())

arr = []
arr.append(0)
for i in range(N):
    arr.append(int(input()))

seg = SegmentTree(arr)
change = []
for i in range(M + K):
    instruction, b, c = map(int, input().split())
    if instruction == 1:
        seg.update(b, c)
    elif instruction == 2:
        print(seg.query(b, c))
