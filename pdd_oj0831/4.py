T = int(input())
for _ in range(T):
    N = int(input())
    a = [int(x) for x in input().split()]
    dp = []
    for i in range(N):
        t = []
        for j in range(N):
            t.append(0)
        dp.append(t)
        dp[i][i] = 1
        if i < N-1:
            dp[i][i+1] = 2
    for w in range(3, N):
        for i in range(N-w):
            j = i+w-1
            m = a[i]
            m_index = i
            for k in range(i+1, j+1):
                if a[k] < m:
                    m = a[k]
                    m_index = k
            dp[i][j] = min(dp[i+1][j-1]+2, m+dp[i][m_index-1]+dp[m_index+1][j])
    print(dp[0][N-1])