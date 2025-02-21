# 변수 선언 및 입력
n, m = map(int, input().split())
s = [0] * (n + 1)
e = [0] * (n + 1)
v = [0] * (n + 1)

# dp[i][j]: i번째 날까지 입을 옷을 전부 결정했고, 마지막 날에 입은 옷이 j번 옷일 때 최소 변화량
dp = [[0] * (n + 1) for _ in range(m + 1)]


def initialize():
    # 첫 번째 날 가능한 옷을 초기화
    for j in range(1, n + 1):
        if s[j] == 1:
            dp[1][j] = 0


# 옷 정보 입력
for i in range(1, n + 1):
    s[i], e[i], v[i] = map(int, input().split())

initialize()

# DP 계산
for i in range(2, m + 1):  # 날짜
    for j in range(1, n + 1):  # 오늘 입을 옷 j
        for k in range(1, n + 1):  # 어제 입었던 옷 k
            # 어제 k번 옷을 입었고, 오늘 j번 옷을 입을 수 있어야 함
            if s[k] <= i - 1 <= e[k] and s[j] <= i <= e[j]:
                dp[i][j] = max(dp[i][j], dp[i - 1][k] + abs(v[j] - v[k]))

# 마지막 날(m)에서 최소 변화량을 가지는 경우 선택
ans = max(dp[m][1:n + 1])

print(ans)
