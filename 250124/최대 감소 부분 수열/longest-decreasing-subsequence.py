n = int(input())
m = list(map(int, input().split()))
dp = [1] * n  # 각 위치에서의 감소 수열 최대 길이

# DP 계산
for i in range(1, n):
    for j in range(i):
        if m[j] > m[i]:  # 감소 조건
            dp[i] = max(dp[i], dp[j] + 1)

# 결과 출력
print((dp))
