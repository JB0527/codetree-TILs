import sys

INT_MAX = sys.maxsize

si = sys.stdin.readline


def preprocess():
    for i in range(m + 1):
        dp[i] = INT_MAX
    dp[0] = 0


n, m = map(int, si().split())
coin = [0] + list(map(int, si().split()))
dp = [0] * (m + 1)

preprocess()

# 금액을 가장 바깥 포문으로 
for i in range(1, m + 1):
    # 동전 종류 순회
    for j in range(1, n + 1):
        # 금액이 동전보다 클 때
        if i >= coin[j]:
            # 도달할 수 없는 금액
            if dp[i - coin[j]] == INT_MAX:
                continue

            # 최소 동전 갱신
            dp[i] = min(dp[i], dp[i-coin[j]] + 1)

ans = dp[m]

#print(dp)

# 도달할 수 없는 금액일 경우
if ans == INT_MAX:
    print(-1)
else:
    print(ans)