def solution(A):
    east = 0
    pairs = 0
    for i in range(len(A)):
        if A[i] == 0:
            east += 1
        else:
            pairs += east
    if pairs > 1000000000:
        return -1
    return pairs