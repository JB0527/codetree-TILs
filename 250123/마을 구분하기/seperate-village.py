from collections import deque

# 입력 받기
n = int(input())  # 격자의 크기 (n x n)
grid = [list(map(int, input().split())) for _ in range(n)]  # 격자 상태 (0 또는 1)

# 방문 여부를 기록하는 배열
visited = [[0 for _ in range(n)] for _ in range(n)]  # 모든 칸을 방문하지 않은 상태로 초기화
groups = []  # 각 그룹(덩어리)의 크기를 저장하는 리스트

# 이동 방향 정의 (상, 하, 좌, 우)
dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

# DFS를 활용하여 연결된 1의 그룹(덩어리)을 찾는 함수
def dfs(i, j):
    visited[i][j] = 1  # 현재 위치를 방문 처리
    count = 1  # 현재 그룹의 크기 (시작점 포함)
    q = deque()  # BFS를 위한 큐 (DFS처럼 작동)
    q.append((i, j))  # 시작점을 큐에 추가

    while q:  # 큐가 빌 때까지 반복
        i, j = q.popleft()  # 큐에서 현재 좌표를 꺼냄
        for dx, dy in zip(dxs, dys):  # 상하좌우 방향으로 이동
            nx, ny = i + dx, j + dy  # 다음 좌표 계산
            if 0 <= nx < n and 0 <= ny < n:  # 격자 범위 안에 있는지 확인
                if grid[nx][ny] == 1 and visited[nx][ny] == 0:  # 연결된 1이고 방문하지 않은 경우
                    visited[nx][ny] = 1  # 방문 처리
                    count += 1  # 그룹 크기 증가
                    q.append((nx, ny))  # 다음 좌표를 큐에 추가
    return count  # 그룹의 크기 반환

# 모든 격자를 순회하며 그룹 탐색
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and visited[i][j] == 0:  # 1이고 방문하지 않은 경우
            groups.append(dfs(i, j))  # 새로운 그룹 발견 -> 크기를 계산해 리스트에 추가

# 그룹 크기를 오름차순으로 정렬
groups = sorted(groups)

# 결과 출력
print(len(groups))  # 총 그룹의 개수 출력
for group_size in groups:  # 각 그룹의 크기를 출력
    print(group_size)
