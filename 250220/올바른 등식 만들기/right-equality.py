n, m = map(int, input().split())
nums = list(map(int, input().split()))

# 이건 메모리 낭비가 너무 심함
"""
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
"""

# 될 수 있는 경우의 수를 고려

dp = [[0]*41 for _ in range(n+1)]
#m이 41가지 경우의 수를 가지므로 ㅇㅇ 기준을 둬버림

dp[0][20] = 1
for i in range(n):
    for j in range(41):
        if dp[i][j] > 0:
            if 0 <= j + nums[i] <41:
                dp[i+1][j + nums[i]] += dp[i][j]
            if 0 <= j - nums[i] <41:
                dp[i+1][j - nums[i]] += dp[i][j]
print(dp[n][20+m])
