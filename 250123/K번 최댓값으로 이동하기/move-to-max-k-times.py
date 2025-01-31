from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# 초기값을 0-based로 변환
r, c = r - 1, c - 1

# 이동 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    curscore = grid[x][y]
    maxscore = 0
    candidates = []

    queue = deque([(x, y)])
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()

        for d in range(4):  # 4방향 탐색
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if grid[nx][ny] < curscore:  # 현재 위치의 스코어보다 낮은 경우만 이동 가능
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    if grid[nx][ny] > maxscore:  # 가장 큰 스코어 업데이트
                        maxscore = grid[nx][ny]
                        candidates = [(nx, ny)]
                    elif grid[nx][ny] == maxscore:  # 최대값이 동일하면 후보 추가
                        candidates.append((nx, ny))
    
    # 후보에서 행 우선, 열 우선 정렬하여 가장 작은 좌표 반환
    if candidates:
        candidates.sort(key=lambda x: (x[0], x[1]))
        return candidates[0]  # 가장 작은 좌표 반환
    else:
        return x, y  # 이동할 곳이 없으면 현재 위치 반환

# k번 이동
for _ in range(k):
    r, c = bfs(r, c)

# 최종 위치 출력 (1-based로 변환)
print(r + 1, c + 1)
