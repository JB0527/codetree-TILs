n,r,c = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

curx,cury = r-1,c-1
compare_num = arr[curx][cury]
visited = [compare_num]

dxs = [-1,1,0,0]
dys = [0,0,-1,1]

def is_in_range(x,y):
    return 0 <=x<n and 0<=y<n

def move():
    global curx, cury, compare_num
    for dx, dy in zip(dxs, dys):
        next_x, next_y = curx + dx, cury + dy
        if is_in_range(next_x, next_y) and arr[next_x][next_y] > compare_num:
            compare_num = arr[next_x][next_y]
            curx,cury = next_x,next_y
            return True

    return False

while move():
    visited.append(arr[curx][cury])

print(*visited)