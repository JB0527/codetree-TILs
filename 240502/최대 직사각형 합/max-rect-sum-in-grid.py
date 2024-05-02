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