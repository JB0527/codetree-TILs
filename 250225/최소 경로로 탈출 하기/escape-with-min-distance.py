from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
step = [[0] * m for _ in range(n)]

ans = 10002
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def bfs(x, y):
    global ans
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        ax, ay = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = ax + dx, ay + dy
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    step[nx][ny] = step[ax][ay] + 1
                    if nx == n - 1 and ny == m - 1:
                        ans = step[n - 1][m - 1] + 1
                    q.append((nx, ny))

bfs(0, 0)

if ans == 10002:
    ans = -1
print(ans)
