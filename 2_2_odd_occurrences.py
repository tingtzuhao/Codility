# none empty array(A) = [N integer, odd number elements]
# each element can be paird with another element that has the same value, leaving just 1 element unpaired

def solution(A):
    num = 0
    for i in range(len(A)):
        num = num ^ A[i]
    print(num)

A = [10, 11, 12, 12, 11, 10, 3, 9, 8, 8, 9]
solution(A)