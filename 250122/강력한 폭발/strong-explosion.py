n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 폭탄 효과를 미리 계산하는 함수
def calculate_effects():
    effects = []
    for i in range(n):
        for j in range(n):
            # 폭탄 1: 세로로 영향을 미침 (i-2, i+2)
            bomb1_effect = {(loc, j) for loc in range(max(0, i - 2), min(n, i + 3))}
            # 폭탄 2: 상하좌우
            bomb2_effect = {(i, j)} | {(i + dx, j + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)] if 0 <= i + dx < n and 0 <= j + dy < n}
            # 폭탄 3: 대각선
            bomb3_effect = {(i, j)} | {(i + dx, j + dy) for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)] if 0 <= i + dx < n and 0 <= j + dy < n}
            effects.append([bomb1_effect, bomb2_effect, bomb3_effect])
    return effects

# 폭탄 효과 미리 계산
effects = calculate_effects()

# 폭탄 위치를 저장
loclist = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]

# 초기화된 최고 점수
best_score = 0

# 최적화된 폭탄 조합 탐색
from itertools import product

for bomb_types in product(range(3), repeat=len(loclist)):
    affected = set()
    for idx, (i, j) in enumerate(loclist):
        bomb_type = bomb_types[idx]
        affected |= effects[i * n + j][bomb_type]  # 해당 폭탄의 효과 적용
    best_score = max(best_score, len(affected))

# 결과 출력
print(best_score)
