from collections import deque

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# grid에서 1은 벽 0은 이동 2는 사람 3은 비피하기 공간임


def bfs(i,j):
    global grid
    dxs=[-1,1,0,0]
    dys=[0,0,-1,1]
    q = deque()
    q.append((i,j,0))
    visited = [
        [False for _ in range(n)]
        for _ in range(n)
    ]
    visited[i][j] = True
    while q:
        x,y,time = q.popleft()
        for dx,dy in zip(dxs,dys):
            newx = dx+x
            newy = dy+y
            if 0<=newx<n and 0<=newy<n and visited[newx][newy] == False:
                # 예외처리 하는 구간
                if grid[newx][newy] == 3:
                    result[i][j] = time+1
                    return
                if grid[newx][newy] != 1:
                    q.append((newx,newy,time+1))
                    visited[newx][newy] = True

result = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            bfs(i,j)

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            if result[i][j] ==0:
                result[i][j] = -1

for i in range(n):
    for j in range(n):
        print(result[i][j],end=" ")
    print()
