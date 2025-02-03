import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력:
n = int(input())
arr = list(map(int, input().split()))

# dp[i] : 점프하여 도착한 위치를 i라 했을 때,
#         가능한 최대 점프 횟수
dp = [0] * n


def initialize():
    # 최댓값을 구하는 문제이므로
    # 초기값은 전부 INT_MIN으로 넣어줍니다.
    for i in range(n):
        dp[i] = INT_MIN
    
    # 시작 위치에서는
    # 가능한 최대 점프 횟수가 0이므로
    # dp[0] = 0이 초기조건이 됩니다.
    dp[0] = 0

   
# 초기조건을 설정합니다.
initialize()

# 점화식에 따라
# 값을 왼쪽에서 오른쪽 방향으로
# 순서대로 채워줍니다.
for i in range(1, n):
    # dp[i] 값은 i번째 보다 앞에 있는 위치(j)들 중 
    # 해당 위치에서 점프하여 i번째 위치로 올 수 있는 경우 중 
    # 최대 점프 가능 횟수를 계산하면 구해집니다. 
    # 이 조건은 j + arr[j] ≥ i임을 
    # 어렵지 않게 알 수 있습니다.
    for j in range(i):
        # dp[j]가 INT_MIN이라면
        # 해당 위치에 이동이 불가능했다는 뜻이므로
        # 계산에서 제외시켜줍니다.
        if dp[j] == INT_MIN:
            continue
        
        if j + arr[j] >= i:
            dp[i] = max(dp[i], dp[j] + 1)

# 이렇게 dp 배열을 전부 채우고 나면
# 각각의 위치를 끝으로 하는 경우를 전부 조사해봐야 하므로 
# dp 배열에 적혀있는 값 들 중 최댓값이 답이 됩니다.
ans = INT_MIN
for i in range(n):
    ans = max(ans, dp[i])

print(ans)
