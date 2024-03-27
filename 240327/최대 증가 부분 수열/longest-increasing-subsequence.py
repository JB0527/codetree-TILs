N = int(input())
lists = [0] + list(map(int,input().split()))
dp = [0 for _ in range(N+1)]

dp[1]=1
for i in range(1,N+1):
    for j in range(i):
        if lists[i] > lists[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))