n, m = map(int, input().split())
nums = list(map(int, input().split()))

# Write your code here!

ans = 0
dp = [[] for _ in range(n+1)]
dp[0].append(0)

for i in range(n):
    for j in range(len(dp[i])):
        if -20 <= dp[i][j] + nums[i] <=20:
            dp[i+1].append(dp[i][j] + nums[i])
        if -20 <= dp[i][j] - nums[i] <=20:
            dp[i+1].append(dp[i][j] - nums[i])



for sol in dp[n]:
    if sol == m:
        ans += 1
print(ans)
