def solution(A):
    counter = 0
    for i in A.sort():
        counter += 1
        if counter != i:
            return 0
    return 1