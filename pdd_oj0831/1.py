T = int(input())
for _ in range(T):
    n, m, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a = sorted(a)
    b = sorted(b)
    res = 0
    j = 0
    xiaochu = 0
    for i in range(n):
        j = xiaochu + 1
        while j < m and abs(a[i] - b[j]) > k:
            j += 1
        if j < m and abs(a[i] - b[j]) <= k:
            res += 1
            xiaochu = j
    print(res)