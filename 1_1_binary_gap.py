def solution(N):
    bi = str(format(N, 'b'))
    res = len(max(bi.strip('0').split('1')))
    return res

solution(529)