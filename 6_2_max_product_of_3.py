def solution(A):
    A.sort()
    r1 = A[-3] * A[-2] * A[-1]
    r2 = A[0] * A[1] * A[-1]
    return max(r1, r2)

A = [-3, 1, 2, -2, 5, 6]
print(solution(A))