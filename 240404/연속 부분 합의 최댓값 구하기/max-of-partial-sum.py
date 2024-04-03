n = int(input())
arr = list[map(int,input().split())]
dp = [0]*(n+1)
dp[1] = 1

for i in range(2,n+1):
    dp[i] = max(dp[i-1] + a[i], 2*a[i])

for i in range(1,n+1):
    ans = max(ans,dp[i])
print(ans)