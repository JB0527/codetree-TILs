n = int(input())

# Write your code here!
mod = (10**9 +7)

dp= [[0]*11 for _ in range(n+1)]
for i in range(1,10):
    dp[1][i] += 1

for i in range(2,n+1):
    for j in range(10):
        dp[i][j] += dp[i-1][j-1]
        dp[i][j] += dp[i-1][j+1]
print((sum(dp[n]))%mod)