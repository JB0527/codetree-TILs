# n, m = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(n)]
# visited = [[False]*n for _ in range(m)]
# dxs = {0,1} #아래
# dys = {1,0} #오른쪽
# # Write your code here!
# ansx,ansy = 0 ,0
# ans = 0
# def dfs(x,y):
#     global ansx,ansy , ans
#     for dx,dy in zip(dxs,dys):
#         curx = x+dx
#         cury = y+dy
#         if 0<=curx<m and 0<=cury<n and visited[curx][cury] == False:
#             if grid[curx][cury] == 1:
#                 visited[curx][cury] = True
#                 # print(visited)
#                 dfs(curx,cury)
#         ansx = curx
#         ansy = cury
#         if ansx == n-1 and ansy ==n-1:
#             ans = 1

# dfs(0,0)
# print(ans)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dxs = [0, 1]  # 아래
dys = [1, 0]  # 오른쪽

ans = 0

def dfs(x, y):
    global ans
    if x == n - 1 and y == m - 1:  # 도착하면 ans를 1로 설정하고 종료
        ans = 1
        return
    
    for dx, dy in zip(dxs, dys):
        curx = x + dx
        cury = y + dy

        if 0 <= curx < n and 0 <= cury < m and not visited[curx][cury]:
            if grid[curx][cury] == 1:
                visited[curx][cury] = True  # 방문 처리
                dfs(curx, cury)
                if ans == 1:  # 목표에 도달했으면 종료
                    return

visited[0][0] = True  # 시작점 방문 처리
dfs(0, 0)
print(ans)
