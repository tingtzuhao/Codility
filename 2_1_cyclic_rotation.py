def solution(A, K):
    if A:
        for i in range(K):
            A.insert(0, A.pop())
        print(A)
    else:
        print([])


A = []
K = 3
solution(A, K)