
s = input()
n = len(s)
if len(s) == 0:
    print(0)
res = 0
dp = []
for i in range(n):
    t = []
    for j in range(n):
        t.append(0)
    dp.append(t)

for j in range(n):
    dp[j][j] = 1
    i = j-1
    while i >= 0:
        if s[i] == s[j]:
            dp[i][j] =  dp[i + 1][j] + dp[i][j - 1]
        else:
            dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
        i -= 1
# print(dp)
print(dp[0][n-1] % 100000007)
