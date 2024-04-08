'''
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
L = [[0,0]]*N
R = [[0,0]]*N

# L 배열을 채워줍니다.
L[0][0] = 0
L[0][1] = 0
for i in range(1, N+1):
    L[i][0] = L[i - 1][0] + abs(arr[i][0] - arr[i - 1][0])
    L[i][1] = L[i - 1][1] + abs(arr[i][1] - arr[i - 1][1])
# R 배열을 채워줍니다.

for i in range(N-1, 0, -1):
    R[i][0] = R[i + 1][0] + abs(arr[i + 1][0] - arr[i][0])
    R[i][1] = R[i + 1][1] + abs(arr[i + 1][1] - arr[i][1])
print(L)
print(R)
print(arr)

min_dist=10002
for i in range(2, n):
    dist_x = (L[i - 1][0] + R[i + 1][0] + abs(arr[i + 1][0] - arr[i - 1][0]))
    dist_y = (L[i - 1][1] + R[i + 1][1] + abs(arr[i + 1][1] - arr[i - 1][1]))
    # print(dist_x, dist_y)
    min_dist = min(min_dist, dist_x + dist_y)

print(min_dist)
'''
import sys


# 체크포인트 한개를 건너 뜀
# 2차원
# 1번 체크포인트와 n번 체크포인트는 건너 뛰지 않는다.
# r배열은 l배열을 단순 뒤집은게 아니다 n-1번 항부터 1번까지 차이를 누적합한 결과이다.


def si():
    return sys.stdin.readline().rstrip()


n = int(si())
a = list([0, 0] for _ in range(n + 1))
l = list([0, 0] for _ in range(n + 1))
r = list([0, 0] for _ in range(n + 1))

for i in range(1, n + 1):
    x, y = map(int, si().split())
    a[i][0], a[i][1] = x, y

for i in range(1, n + 1):
    l[i][0] = l[i-1][0] + abs(a[i][0] - a[i - 1][0])
    l[i][1] = l[i-1][1] + abs(a[i][1] - a[i - 1][1])

for i in range(n, 1, -1):
    r[i-1][0] = r[i][0] + abs(a[i][0] - a[i-1][0])
    r[i-1][1] = r[i][1] + abs(a[i][1] - a[i-1][1])



# print(a)
# print(l)
# print(r)

# 맨하탄 거리
min_dist = sys.maxsize
for i in range(2, n):
    dist_x = (l[i - 1][0] + r[i + 1][0] + abs(a[i + 1][0] - a[i - 1][0]))
    dist_y = (l[i - 1][1] + r[i + 1][1] + abs(a[i + 1][1] - a[i - 1][1]))
    # print(dist_x, dist_y)
    min_dist = min(min_dist, dist_x + dist_y)

print(min_dist)