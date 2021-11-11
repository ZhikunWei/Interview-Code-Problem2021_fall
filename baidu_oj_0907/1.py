N, W = [int(x) for x in input().split()]
weight = [0]
val = [0]

for _ in range(N):
    w, v = [int(x) for x in input().split()]
    weight.append(w)
    weight.append(w)
    val.append(v)
    val.append(v)

dp = []
for i in range(N*2+1):
    t = []
    for _ in range(W+1):
        t.append(0)
    dp.append(t)

res = 0
for i in range(1, N*2+1):
    for j in range(1, W+1):
        if weight[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-weight[i]]+val[i], dp[i-1][j])

        res = max(res, dp[i][j])
print(res)