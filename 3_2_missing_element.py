def solution(A):
    if not A:
        return 1
    return sum(range(1, len(A)+2)) - sum(A)

A = [1, 2, 4]
T = [1, 2, 3, 4]
# A = []
print(solution(A))
# print(range(1, len([1, 2, 4])+2)) 