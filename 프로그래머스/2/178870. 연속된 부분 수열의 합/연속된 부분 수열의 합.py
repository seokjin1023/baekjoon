def solution(sequence, k):
    answer = [0, 0]
    start = 0
    end = 0
    part_sum = sequence[0]
    min_length = 1_000_001
    for i in range(1, len(sequence) + 1):
        while part_sum > k:
            part_sum -= sequence[start]
            start += 1
        if part_sum == k:
            if end - start + 1 > 0 and min_length > end - start + 1:
                answer[0] = start
                answer[1] = end
                min_length = end - start + 1
        if i == len(sequence):
            break
        part_sum += sequence[i]
        end += 1
    return answer