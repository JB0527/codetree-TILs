import sys
input = sys.stdin.readline
n= int(input())

arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

def dfs(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and arr[nx][ny] > arr[x][y]:
            value = visited[x][y] + 1
            if visited[nx][ny] < value:
                visited[nx][ny] = value
                dfs(nx, ny)
                
    return

for x in range(n):
    for y in range(n):
        if visited[x][y] == 0:
            dfs(x,y)
print(max(map(max,visited))+1)