n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs = {0,1} #아래
dys = {1,0} #오른쪽
# Write your code here!
ansx,ansy = 0 ,0
ans = 0
def dfs(x,y):
    global ansx,ansy , ans
    for dx,dy in zip(dxs,dys):
        curx = x+dx
        cury = y+dy
        if 0<=curx<n and 0<=cury<n:
            if grid[curx][cury] == 1:
                dfs(curx,cury)
        ansx = curx
        ansy = cury
        if ansx == n-1 and ansy ==n-1:
            ans = 1

dfs(0,0)  
print(ans)