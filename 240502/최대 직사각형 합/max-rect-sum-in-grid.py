"""
import sys
INT_MIN = -sys.maxsize
ans = INT_MIN

n= int(input())
arr = [[0]*(n+1)]+[[0]+list(map(int,input().split())) for _ in range(n)]
prefix_sum = [[0]*(n+1) for _ in range(n+1)]

#print(arr)

# (x1, y1), (x2, y2) 직사각형 구간 내의 원소의 합을 반환합니다.
def get_size(i, j, k, l):
    return prefix_sum[k][l] - prefix_sum[k][j - 1] - prefix_sum[i - 1][l] + prefix_sum[i - 1][j - 1]

# 누적합 배열을 만들어줍니다.
prefix_sum[0][0] = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + \
                           prefix_sum[i][j - 1] - \
                           prefix_sum[i - 1][j - 1] + \
                           arr[i][j]
#print(prefix_sum)

#각 위치마다의 사각형의 합을 첫번쨰요소로 두고 생각.

#여길 못하겟어이이이잉이이이


for i in range(1, n + 1):
    for j in range(1, n + 1):
        ans = max(ans, max_square[i][j][0])

print(ans)
"""
import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력:
n = int(input())

arr = [[0] * (n + 1)]
for _ in range(n):
    arr.append([0] + list(map(int, input().split())))

prefix_sum = [
    [0] * (n + 1)
    for _ in range(n + 1)
]


# (x1, y1), (x2, y2) 직사각형 구간 내의 원소의 합을 반환합니다.
def get_sum(x1, y1, x2, y2):
    return prefix_sum[x2][y2]     - prefix_sum[x1 - 1][y2] - \
           prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1]


# 시작행이 x1, 끝 행이 x2인 직사각형 중
# 가능한 최대 합을 반환합니다.
def get_max_area(x1, x2):
    # 시작행과 끝 행이 x1, x2로 정해지면,
    # 각 열마다 x1부터 x2까지 행에 적혀있는 숫자들을 누적했을 때
    # 마치 1차원에서 최대 연속 부분 수열의 합을 구하는 문제와 같아집니다.
    # 이는 동적계획법으로 간단히 해결이 가능합니다.
    dp = [0] * (n + 1)

    for y in range(1, n + 1):
        # y열에 있는 숫자들의 합을 구해줍니다.
        value = get_sum(x1, y, x2, y)
        dp[y] = max(value, dp[y - 1] + value)

    # dp 값 중 최댓값이 원하는 값이 됩니다.
    max_area = INT_MIN
    for y in range(1, n + 1):
        max_area = max(max_area, dp[y])
    
    return max_area


# 누적합 배열을 만들어줍니다.
prefix_sum[0][0] = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + \
                           prefix_sum[i][j - 1] - \
                           prefix_sum[i - 1][j - 1] + \
                           arr[i][j]

# 직사각형의
# 시작 행과 끝 행을 결정합니다.
# 각 쌍에 대해 가능한 직사각형 중
# 최대 합을 계산해
# 답과 비교하여 최댓값을 갱신해줍니다.
ans = INT_MIN
for i in range(1, n + 1):
    for j in range(i, n + 1):
        ans = max(ans, get_max_area(i, j))

print(ans)