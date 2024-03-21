import sys
input = sys.stdin.readline
n = int(input())
df = []

a = [list(map(int,input().split())) for _ in range(n)]

# 초깃값
dp[0][0] = a[0][0]

for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + a[i][0]

    dp[i][i] = dp[i - 1][i - 1] + a[i][i]

for i in range(2, n):
    for j in range(1, i):     

        case_1 = dp[i - 1][j - 1] + a[i][j]
        case_2 = dp[i - 1][j] + a[i][j]
        dp[i][j] = max(case_1, case_2)


for i in range(n):
    for j in range(i):
        print(dp[i][j], end='\t')
    print()