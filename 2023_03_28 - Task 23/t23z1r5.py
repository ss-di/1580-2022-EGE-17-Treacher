f = 1
t = 20

dp = [-1] * (t + 1)
dp[f] = 1
for x in range(f + 1, t + 1):
    dp[x] = dp[x - 1]
    if x % 3 == 0:
        dp[x] += dp[x // 3]

print(dp[t])
