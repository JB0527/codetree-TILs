NUM_STATE = 2
MIN_ANS = -500000

NOT_BELONG = 0
BELONG = 1
    
# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
a = [
    0
    for _ in range(n + 1)
]

# dp[i][j][k] : i번째 위치까지 잘 고려하여,
#               총 j개의 구간을 선택했고
#               i번째가 마지막 구간에 속하지 않았다면 k = NOT_BELONG
#               i번째가 마지막 구간에 속했다면 k = BELONG 상태라 했을 때
#               얻을 수 있는 합의 최대
dp = [
    [
        [0 for i in range(NUM_STATE + 1)]
        for _ in range(m + 1)
    ]
    for _ in range(n + 1)
]


def initialize():
    # 최댓값을 구하는 문제이므로, 
    # 초기에는 전부
    # 답이 될 수 있는 최솟값인 MIN_ANS 넣어줍니다.
    for i in range(0, n + 1):
        for j in range(0, m + 1):
            dp[i][j][NOT_BELONG] = dp[i][j][BELONG] = MIN_ANS
    
    # 선택한 구간의 수가 0개일 때를
    # 초기 조건으로 설정합니다.
    # 0에서 n 사이의 모든 위치 i에 대해
    # 선택한 구간의 수가 0개이고
    # 해당 원소는 구간에 사용하지 않았으며
    # 선택한 구간이 없으므로 초기 합은 0이기 때문에
    # dp[i][0][NOT_BELONG] = 0이 됩니다.
    for i in range(0, n + 1):
        dp[i][0][NOT_BELONG] = 0


given_seq = list(map(int, input().split()))
a[1:] = given_seq[:]

initialize()

# i번째 위치까지 잘 고려하여,
# 총 j개의 구간을 선택했을 때,
# 얻을 수 있는 최대 합을 계산합니다.

for i in range(1, n + 1):
    for j in range(1, m + 1):
        # i번째 숫자를 구간에 포함 시켰는지, 안 시켰는지에 대하여
        # 각각 점화식을 세워줍니다.

        # Case 1
        # i번째 숫자를 구간에 포함시킨 경우입니다. (BELONG)
        # 이때 또 선택지가 2개로 나뉩니다. 다음 2가지 중
        # 더 좋은 값을 택하면 됩니다.

        # Case 1 - 1
        # 만약 i번째 숫자가 새로운 구간의 시작이라면
        # 이전 구간이랑 인접하지 않아야 하므로 i - 1번째 상태가
        # NOT_BELONG이어야 하며, 그떄까지 j - 1개의 구간을 
        # 선택했을 경우에 해당하는 
        # dp[i - 1][j - 1][NOT_BELONG]에 a[i] 를 더합니다.

        # Case 1 - 2
        # 만약 i번째 숫자를 이전 j번째 구간에 포함시키려고 한다면
        # i - 1번째 상태가 BELONG이어야 하며, 그때까지 j개의
        # 구간을 선택했을 경우에 해당하는
        # dp[i - 1][j][BELONG]에 a[i]를 더합니다.
        
        dp[i][j][BELONG] = max(dp[i - 1][j - 1][NOT_BELONG] + a[i],
                                   dp[i - 1][j][BELONG] + a[i])
        
        # Case 2
        # i번째 숫자를 구간에 포함시키지 않은 경우입니다. (NOT_BELONG)
        # 이때는 i - 1번째 원소를 j번째 구간에 포함시켰는지에 대한 여부가
        # 크게 중요하지 않으므로
        # dp[i - 1][j][NOT_BELONG]과 dp[i - 1][j][BELONG] 중
        # 더 좋은 값을 선택하면 됩니다.
        dp[i][j][NOT_BELONG] = max(dp[i - 1][j][NOT_BELONG],
                                       dp[i - 1][j][BELONG])

# n번째 위치까지 고려했을 때
# 정확히 m개의 구간을 선택해야 하며
# 마지막 원소가 m번째 구간에 들어갔는지, 들어가지 않았는지 여부는
# 크게 상관 없으므로 두 경우 중 값이 더 큰 경우를 선택합니다.
print(max(dp[n][m][NOT_BELONG], dp[n][m][BELONG]))
