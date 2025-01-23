n = int(input())
dp = [0 for _ in range(n+1)]
# # Write your code here!
dp[0] = 1
dp[1] = 1
# n = 1 일때, 1
# n= 2 일대, 2
# n = 3 일대 3
# n =4일대 , 2 3 5

for i in range(1,n):
    dp[i+1] = dp[i]+dp[i-1]

result = (dp[n] %10007)
print(result)