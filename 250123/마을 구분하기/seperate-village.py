from collections import deque
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
# Write your code here!
visited = [[0 for _ in range(n)] for _ in range(n)]
groups = []

dxs =[0,0,-1,1]
dys =[-1,1,0,0]

def dfs(i,j):
    visited[i][j]= 1
    count = 1
    q = deque()
    q.append((i,j))
    while q:
        i,j = q.popleft()
        for dx,dy in zip(dxs,dys):
            if 0<=i+dx<n and 0<=j+dy<n:
                if grid[i+dx][j+dy] == 1 and visited[i+dx][j+dy]==0:
                    visited[i+dx][j+dy] = 1
                    count +=1
                    q.append((i+dx,j+dy))
    return count

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and visited[i][j]==0:
            groups.append(dfs(i,j))
groups = sorted(groups)
print(len(groups))
for _ in (groups):
    print(_)