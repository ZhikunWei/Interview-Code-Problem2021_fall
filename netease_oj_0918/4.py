# TLE 50%
cache = {}
def real6(val):
    global cache
    has6 = 0
    has8 = 0
    x = val
    while x > 0:
        if x in cache:
            has6 += cache[x][0]
            has8 += cache[x][1]
            if has8 > 0:
                return has6
            else:
                return 0
        xx = x % 10
        if xx == 6:
            has6 += 1
        if xx == 8:
            has8 += 1
        x = x // 10
    
    ca6 = has6
    ca8 = has8
    xx = val % 10
    if xx == 6:
        ca6 -= 1
    if xx == 8:
        ca8 -= 1
    val = val // 10
    cache[val] = [ca6, ca8]
    # while val > 0:
    #     if val in cache:
    #         break
    #     cache[val] = [ca6, ca8]
    #     xx = val % 10
    #     if xx == 6:
    #         ca6 -= 1
    #     if xx == 8:
    #         ca8 -= 1
    #     val = val // 10
    if has8 > 0:
        return has6
    else:
        return 0


t = int(input())
for _ in range(t):
    a, b = [int(x) for x in input().split()]
    res = 0
    for i in range(a, b + 1):
        res += real6(i)
    print(res)
