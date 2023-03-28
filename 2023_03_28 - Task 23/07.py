f = 25
t = 51

dp = [0] * (t+1)
dp[f] = 1
for x in range(f + 1, t + 1):
    dp[x] = dp[x - 1]
    if x % 10 > 0:
        d = x // 10
        e = x % 10
        y = (d-1)*10 + e-1
        dp[x] += dp[y]
        if e == 9:
            y = (d-1)*10 + e
            dp[x] += dp[y]

print(dp[t])