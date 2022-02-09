# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    rng = range(min(A), max(A))
    lst = [num for num in rng if num not in A]
    if not lst:
        res = max(A) + 1
    elif min(lst) <= 0:
        res = 1
    else:
        res = min(lst)
    print(res)

A = range(1, 1000001)
solution(A)