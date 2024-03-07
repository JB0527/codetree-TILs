import collections
n, m = map(int, input().split())


tmp = []
for i in range(n):
    tmp.append(list(map(int,input().split())))

grid = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        grid[i][j].append(tmp[i][j])

order = list(map(int,input().split()))


dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

# 격자 내에 있는지 체크
def in_range(x, y) :
    return 0 <= x < n and 0 <= y < n


for num in order:
    pos = False
    for x in range(n):
        for y in range(n):
            #print("grid[x][y]", grid[x][y], len(grid[x][y]), num)
            #print(grid)
            if len(grid[x][y]) == 0:
                continue
            
            if num in grid[x][y]:
                max_val = 0
                max_x,max_y = x,y

                for i in range(8):
                    nx = x + dxs[i]
                    ny = y + dys[i]

                    if not in_range(nx, ny):
                        continue

                    if len(grid[nx][ny]) == 0:
                        continue
                    if max_val <= max(grid[nx][ny]):
                        max_val = max(grid[nx][ny])
                        max_x,max_y = nx,ny
                # 새로 옮겨지면 기존의 숫자 위에 옮겨진다 => idx가 앞으로 채워진다
                idx = 0 
                for i, val in enumerate(grid[x][y]):
                    if val == num:
                        idx = i
                
                grid[max_x][max_y] = grid[x][y][:idx+1] + grid[max_x][max_y]
                # 옮겨진거 이후의 것들은 그대로 남아 있어야 한다 ( slicing의 범위 잘 체크 하기 )
                grid[x][y] = grid[x][y][idx+1:]

                pos = True
                break

        if pos:
            break

for i in range(n):
    for j in range(n):
        if not grid[i][j]:
            print("None")
        else:
            print(*grid[i][j])