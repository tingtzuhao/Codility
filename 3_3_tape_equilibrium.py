def solution(A):
    total = sum(A)
    dif = float('inf')
    left_sum = 0
    for i in A[:-1]:
        left_sum += i
        dif = min(abs(total - 2 * left_sum), dif)
    return dif

A = [3, 1, 2, 4, 3]
print(solution(A))