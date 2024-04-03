import sys
INT_MIN = -sys.maxsize
n = int(input())
arr = list(map(int,input().split()))
dp = [0]*(n+1)

dp[1] = arr[0]
for i in range(2,n):
    dp[i] = max(dp[i-1] + arr[i], arr[i])

ans = -10002
for i in range(1,n+1):
    ans = max(ans,dp[i])
print(ans)