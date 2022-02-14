def solution(A):
    check = []
    if not A:
        return 1
    elif A[0] in ')}]':
        return 0
    for brk in A:
        if brk in '({[':
            check.append(brk)
        elif brk == ')' and not check:
            return 0
        elif brk == '}' and not check:
            return 0
        elif brk == ']' and not check:
            return 0
        elif brk == ')' and check[-1] == '(':
            check.pop()
        elif brk == '}' and check[-1] == '{':
            check.pop()
        elif brk == ']' and check[-1] == '[':
            check.pop()
    if check:
        return 0
    return 1