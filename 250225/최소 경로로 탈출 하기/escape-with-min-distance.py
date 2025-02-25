from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]
# Write your code here!
step = [[0 for _ in range(m)] for _ in range(n)]


ans = 10002
def bfs(x,y):
    global ans
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q:
        ax,ay = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx = ax+dx
            ny = ay+dy
            if 0<=nx<n and 0<=ny<m :
                if arr[nx][ny]==1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    step[nx][ny] += (step[ax][ay]+1)
                    if nx == m-1 and ny == n-1:
                        ans = step[m-1][n-1]
                    q.append((nx,ny))

dxs = [0,1,0,-1]
dys = [1,0,-1,0]


bfs(0,0)

if ans == 10002:
    ans = -1
print(ans)

