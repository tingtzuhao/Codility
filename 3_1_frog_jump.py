def solution(X, Y, D):
    # write your code in Python 3.6
    dist = Y - X
    steps = dist // D
    if X + steps * D < Y:
        steps += 1
    return steps