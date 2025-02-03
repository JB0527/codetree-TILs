n = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(n)]

# Write your code here!
dp[0] = 0
jump = 0
for idx,value in enumerate(arr):
    if value >= 1:
        for j in range(1,value+1):
            if idx+j <n:
                dp[idx+j] = max(dp[idx+j],dp[idx] + 1)
        if idx < n-1:
            if max(arr[idx+1:idx+j+1]) == 0:
                break
print(max(dp))
