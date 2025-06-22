from collections import Counter

def solution(weights):
    cnt = Counter(weights)
    answer = 0


    for w, c in cnt.items():
        answer += c * (c - 1) // 2

    distances = [2, 3, 4]
    for d1 in distances:
        for d2 in distances:
            if d1 == d2:
                continue

            for w in cnt:
                if (w * d1) % d2 != 0:
                    continue

                w2 = (w * d1) // d2
                if w < w2 and w2 in cnt:
                    answer += cnt[w] * cnt[w2]

    return answer