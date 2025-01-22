n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def apply_bomb1(i, j, affected):
    """폭탄 1 적용"""
    for loc in range(max(i-2,j), min(i+3, j)):
        affected.add((loc, j))
    return affected

def apply_bomb2(i, j, affected):
    """폭탄 2 적용"""
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    affected.add((i, j))
    for dx, dy in directions:
        x, y = i + dx, j + dy
        if 0 <= x < n and 0 <= y < n:
            affected.add((x, y))
    return affected

def apply_bomb3(i, j, affected):
    """폭탄 3 적용"""
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    affected.add((i, j))
    for dx, dy in directions:
        x, y = i + dx, j + dy
        if 0 <= x < n and 0 <= y < n:
            affected.add((x, y))
    return affected

def calculate_score(affected):
    """폭탄 배열에서 영향을 받은 셀의 총합 계산"""
    return len(affected)

# 폭탄 위치를 저장
loclist = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]

# 초기화된 최고 점수
best_score = 0
final_bombarr = [[0] * n for _ in range(n)]

# 폭탄 위치에 대해 모든 조합을 탐색
for bomb_type_combination in range(3 ** len(loclist)):
    affected = set()  # 중복을 방지하기 위한 집합
    temp_combination = bomb_type_combination
    for (i, j) in loclist:
        bomb_type = temp_combination % 3  # 0: bomb1, 1: bomb2, 2: bomb3
        temp_combination //= 3
        if bomb_type == 0:
            affected = apply_bomb1(i, j, affected)
        elif bomb_type == 1:
            affected = apply_bomb2(i, j, affected)
        elif bomb_type == 2:
            affected = apply_bomb3(i, j, affected)
    
    # 현재 조합의 점수 계산
    current_score = calculate_score(affected)
    if current_score > best_score:
        best_score = current_score
        final_bombarr = [[1 if (i, j) in affected else 0 for j in range(n)] for i in range(n)]


print(best_score)
"""
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
def bomb1(i,j):
    bombarr[i][j] = 1
    for loc in range(j-2,j+2):
        if j-n >=0 and j+n <=n:
            bombarr[i][loc] = 1

def bomb2(i,j):
    bombarr[i][j] = 1
    dxs = [-1,-1,1,1]
    dxy = [0,0,1,1]
    for dx,dy in zip(dxs,dxy):
        bombarr[i+dx][j+dy] = 1

def bomb3(i,j):
    bombarr[i][j] = 1
    dxs = [-1,-1,1,1]
    dxy = [-1,1,-1,1]
    for dx,dy in zip(dxs,dxy):
        bombarr[i+dx][j+dy] = 1

total = 0
loclist = []
bombarr = [ 0*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            loclist.append((i,j))



while loclist == None:
    for (i,j) in loclist:
        bomb1(i,j)

        total = max(total,new_total)

print(total)

"""