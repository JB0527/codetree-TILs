n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def find_max(start_r, start_c):
    dx = [0, 0, 1, -1]  # 동, 서, 남, 북
    dy = [1, -1, 0, 0]
    total = grid[start_r][start_c]  # 시작 지점의 값
    neighbors = []
    
    # 유효한 이웃 값 수집
    for dxs, dys in zip(dx, dy):
        nr, nc = start_r + dxs, start_c + dys
        if 0 <= nr < n and 0 <= nc < m:  # 그리드 범위 체크
            neighbors.append((grid[nr][nc], nr, nc))
    
    if len(neighbors) < 2:  # 유효한 이웃이 2개 미만이면 계산 불가
        return total
    
    # 이웃을 값 기준으로 내림차순 정렬
    neighbors.sort(reverse=True, key=lambda x: x[0])
    total += neighbors[0][0]  # 가장 큰 이웃 값 추가
    new_r, new_c = neighbors[0][1], neighbors[0][2]  # 해당 좌표 저장
    
    # 세 번째 값 찾기 (시작 지점과 가장 큰 이웃 제외)
    third_max = -1
    for dxs, dys in zip(dx, dy):
        nr, nc = new_r + dxs, new_c + dys
        if 0 <= nr < n and 0 <= nc < m and (nr, nc) != (start_r, start_c):
            third_max = max(third_max, grid[nr][nc])
    
    if third_max > 0:  # 세 번째 값이 유효하면 추가
        total += third_max
    return total

max_value = 0

# 모든 셀에 대해 최대값 계산
for row in range(n):
    for col in range(m):
        max_value = max(max_value, find_max(row, col))

print(max_value)

"""
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def find_max(start_r,start_c):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    total = grid[start_r][start_c]
    new_max = 0
    arr = [] #3번째 위치찾기를 위해서
    for dxs,dys in dx,dy:
        new_value = grid[start_r+dxs][start_c+dys]
        arr.append(new_value)
        
        new_max = max(new_max,new_value)
        if new_max == new_value:
            new_r,new_c = start_r+dxs,start_c+dys
        arr.remove(new_max) #이미 지정된 max값 제외
    total += new_max
    # 세번째 위치찾기
    third_max = 0
    for dxs,dys in dx,dy:
        new_value = grid[new_r+dxs][new_c+dys]
        if new_r+dxs,new_c+dys != start_r,start_c:
            continue
        arr.append(new_value)
    total += max(arr)
    return total
max_value = 0
# Write your code here!
for row in range(m):
    for col in range(n):
        if row+1 <= m and col+1 <= n:
            continue
        value = grid[row][col]

        max_value = max(max_value,value)
        if value == max_value:
           real_row,real_col = row,col

print(find_max(real_row,real_col))
"""