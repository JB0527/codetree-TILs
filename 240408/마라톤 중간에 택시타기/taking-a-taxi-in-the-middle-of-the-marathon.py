import sys

INT_MAX = sys.maxsize
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
L = [0]*N
R = [0]*N

# L 배열을 채워줍니다.
L[0] = 0
for i in range(1, N):
    L[i] = L[i - 1] + abs(arr[i][0] - arr[i - 1][0]) + abs(arr[i][1] - arr[i - 1][1])
# R 배열을 채워줍니다.
R[N-1] = 0
for i in range(N-2, -1, -1):
    R[i] = R[i + 1] + abs(arr[i + 1][0] - arr[i][0]) + abs(arr[i+1][1] - arr[i][1])
print(L)
print(R)
print(arr)
ans = INT_MAX
for i in range(1, N- 1):
    ans = min(ans, L[i - 1] + R[i + 1] + abs(arr[i + 1][0] - arr[i - 1][0]) + abs(arr[i + 1][1] - arr[i - 1][1]))

print(ans)