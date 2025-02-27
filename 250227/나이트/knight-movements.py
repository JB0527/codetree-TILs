from collections import deque
n = int(input())
r1, c1, r2, c2 = map(int, input().split())

visited = [[False for _ in range(n)] for _ in range(n)]
# Please write your code here.

dxs = [-1,-1,-2,-2,1,1,2,2]
dys = [-2,2,-1,1,-2,2,-1,1]

def bfs(i,j,step):
    q= deque()
    q.append((i,j,step))
    while q:
        i,j,step = q.popleft()
        if i == r2-1 and j ==c2-1:
            return step
        for dy,dx in zip(dys,dxs):
            ny = dy+j
            nx = dx+i
            if 0<=nx<n and 0<=ny<n :
                if visited[nx][ny] == False:
                    q.append((nx,ny,step+1))
                    visited[nx][ny] = True
    return step
visited[r1-1][c1-1] = True
ans = bfs(r1-1,c1-1,0)

if not visited[r2-1][c2-1]:
    print(-1)
else:
    print(ans)