import sys
from collections import deque

MAXN = 20
MAXM = 20
MAXF = 400
MAXP = MAXF * 6

INF = int(1e9 + 10)

# 전역 배열 선언
SpaceMap = [[0 for _ in range(MAXN + 10)] for _ in range(MAXN + 10)]
SpaceMapCellId = [[0 for _ in range(MAXN + 10)] for _ in range(MAXN + 10)]
TimeWall = [[[0 for _ in range(MAXM + 10)] for _ in range(MAXM + 10)] for _ in range(6)]
TimeWallCellId = [[[0 for _ in range(MAXM + 10)] for _ in range(MAXM + 10)] for _ in range(6)]

# 클래스 대신 이벤트 정보를 사전으로 저장 (인덱스 1부터 사용)
events = [{"xpos": 0, "ypos": 0, "direction": 0, "cycle": 0, "alive": 0} for _ in range(MAXF + 10)]

Graph = []  # 인접리스트 형태의 그래프

def build_graph(N, M):
    global Graph, SpaceMapCellId, TimeWallCellId
    cnt = 0

    # 평면도에서 시간의 벽(값 3)이 아닌 셀에 번호 부여
    for i in range(N):
        for j in range(N):
            if SpaceMap[i][j] != 3:
                cnt += 1
                SpaceMapCellId[i][j] = cnt

    # 단면도 (동, 남, 서, 북, 위 순) 각 셀에 번호 부여
    for t in range(5):
        for i in range(M):
            for j in range(M):
                cnt += 1
                TimeWallCellId[t][i][j] = cnt

    # 번호에 해당하는 정점들에 대해 4방향 (-1: 연결 없음) 초기화
    Graph = [[-1 for _ in range(4)] for _ in range(cnt + 1)]

    # 동, 남, 서, 북 순 (인덱스 0~3)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # [1] 평면도(시간의 벽이 없는 부분) 인접 셀 연결
    for i in range(N):
        for j in range(N):
            if SpaceMap[i][j] != 3:
                idx = SpaceMapCellId[i][j]
                for dd in range(4):
                    nx = i + dx[dd]
                    ny = j + dy[dd]
                    if nx < 0 or ny < 0 or nx >= N or ny >= N:
                        continue
                    if SpaceMap[nx][ny] == 3:
                        continue
                    Graph[idx][dd] = SpaceMapCellId[nx][ny]

    # [2] 단면도의 동, 남, 서, 북 면에 대해 연결
    for t in range(4):
        for i in range(M):
            for j in range(M):
                idx = TimeWallCellId[t][i][j]
                for dd in range(4):
                    nx = i + dx[dd]
                    ny = j + dy[dd]
                    if nx < 0 or nx >= M:
                        continue
                    if ny < 0:
                        # 시계방향으로 한 면 앞쪽 (오른쪽 끝) 셀과 연결
                        Graph[idx][dd] = TimeWallCellId[(t + 1) % 4][nx][M - 1]
                    elif ny >= M:
                        Graph[idx][dd] = TimeWallCellId[(t + 3) % 4][nx][0]
                    else:
                        Graph[idx][dd] = TimeWallCellId[t][nx][ny]

    # [3] 위쪽 단면도 내부의 인접 셀 연결 (4번 단면)
    for i in range(M):
        for j in range(M):
            idx = TimeWallCellId[4][i][j]
            for dd in range(4):
                nx = i + dx[dd]
                ny = j + dy[dd]
                if nx < 0 or ny < 0 or nx >= M or ny >= M:
                    continue
                Graph[idx][dd] = TimeWallCellId[4][nx][ny]

    # [4] 위쪽 단면도와 인접한 다른 단면도 연결
    # 동쪽 단면도와 연결
    for i in range(M):
        idx = TimeWallCellId[4][i][M - 1]       # 위쪽 단면도의 오른쪽 끝 셀
        idy = TimeWallCellId[0][0][M - 1 - i]     # 동쪽 단면도의 대응 셀
        Graph[idx][0] = idy
        Graph[idy][3] = idx
    # 남쪽 단면도와 연결
    for i in range(M):
        idx = TimeWallCellId[4][M - 1][i]         # 위쪽 단면도의 아래쪽 셀
        idy = TimeWallCellId[1][0][i]             # 남쪽 단면도의 대응 셀
        Graph[idx][1] = idy
        Graph[idy][3] = idx
    # 서쪽 단면도와 연결
    for i in range(M):
        idx = TimeWallCellId[4][i][0]             # 위쪽 단면도의 왼쪽 끝 셀
        idy = TimeWallCellId[2][0][i]             # 서쪽 단면도의 대응 셀
        Graph[idx][2] = idy
        Graph[idy][3] = idx
    # 북쪽 단면도와 연결
    for i in range(M):
        idx = TimeWallCellId[4][0][i]             # 위쪽 단면도의 위쪽 셀
        idy = TimeWallCellId[3][0][M - 1 - i]       # 북쪽 단면도의 대응 셀
        Graph[idx][3] = idy
        Graph[idy][3] = idx

    # [5] 평면도에서 시간의 벽(값 3)이 시작하는 위치 탐색
    timewallStartx = -1
    timewallStarty = -1
    for i in range(N):
        for j in range(N):
            if SpaceMap[i][j] == 3:
                timewallStartx = i
                timewallStarty = j
                break
        if timewallStartx != -1:
            break

    # [6] 평면도와 단면도의 경계 연결
    # 동쪽 단면도와 연결 (평면도 오른쪽)
    if timewallStarty + M < N:
        for i in range(M):
            idx = TimeWallCellId[0][M - 1][i]
            idy = SpaceMapCellId[timewallStartx + (M - 1) - i][timewallStarty + M]
            Graph[idx][1] = idy
            Graph[idy][2] = idx
    # 남쪽 단면도와 연결 (평면도 아래쪽)
    if timewallStartx + M < N:
        for i in range(M):
            idx = TimeWallCellId[1][M - 1][i]
            idy = SpaceMapCellId[timewallStartx + M][timewallStarty + i]
            Graph[idx][1] = idy
            Graph[idy][3] = idx
    # 서쪽 단면도와 연결 (평면도 왼쪽)
    if timewallStarty > 0:
        for i in range(M):
            idx = TimeWallCellId[2][M - 1][i]
            idy = SpaceMapCellId[timewallStartx + i][timewallStarty - 1]
            Graph[idx][1] = idy
            Graph[idy][0] = idx
    # 북쪽 단면도와 연결 (평면도 위쪽)
    if timewallStartx > 0:
        for i in range(M):
            idx = TimeWallCellId[3][M - 1][i]
            idy = SpaceMapCellId[timewallStartx - 1][timewallStarty + (M - 1) - i]
            Graph[idx][1] = idy
            Graph[idy][1] = idx

    return cnt

# 입력 처리
N, M, E = map(int, input().split())

# [A] 평면도 입력
for i in range(N):
    SpaceMap[i][:N] = list(map(int, input().split()))

# [B] 시간의 벽 단면도 입력
# 동쪽 단면도
for i in range(M):
    TimeWall[0][i][:M] = list(map(int, input().split()))
# 서쪽 단면도 (편의를 위해 TimeWall[2]에 저장)
for i in range(M):
    TimeWall[2][i][:M] = list(map(int, input().split()))
# 남쪽 단면도 (TimeWall[1])
for i in range(M):
    TimeWall[1][i][:M] = list(map(int, input().split()))
# 북쪽 단면도 (TimeWall[3])
for i in range(M):
    TimeWall[3][i][:M] = list(map(int, input().split()))
# 위쪽 단면도 (TimeWall[4])
for i in range(M):
    TimeWall[4][i][:M] = list(map(int, input().split()))

# [C] 시간 이상 현상 이벤트 정보 입력
for i in range(1, E + 1):
    x, y, direction, cycle = map(int, input().split())
    events[i]["xpos"] = x
    events[i]["ypos"] = y
    events[i]["direction"] = direction
    events[i]["cycle"] = cycle
    # 입력에서 1과 2의 방향을 서로 교환
    if events[i]["direction"] == 1:
        events[i]["direction"] = 2
    elif events[i]["direction"] == 2:
        events[i]["direction"] = 1
    events[i]["alive"] = 1

cnt = build_graph(N, M)

# 거리 배열 (정점 번호 1 ~ cnt), 미방문은 -1
dist = [-1] * (cnt + 1)

# [D] 평면도 상의 장애물 처리 (값 1은 장애물)
for i in range(N):
    for j in range(N):
        if SpaceMap[i][j] == 3:
            continue
        if SpaceMap[i][j] == 1:
            idx = SpaceMapCellId[i][j]
            dist[idx] = INF

# 이벤트 시작점(시간 이상 현상 시작점)은 도달 불가능하므로 INF 처리
for i in range(1, E + 1):
    x = events[i]["xpos"]
    y = events[i]["ypos"]
    idx = SpaceMapCellId[x][y]
    dist[idx] = INF

# [E] 단면도 상의 장애물 처리 (값 1)
for t in range(5):
    for i in range(M):
        for j in range(M):
            if TimeWall[t][i][j] == 1:
                idx = TimeWallCellId[t][i][j]
                dist[idx] = INF

# [F] 탈출구와 타임머신 시작점 탐색
cell_start = -1
cell_end = -1
# 탈출구: 평면도에서 값이 4인 셀
for i in range(N):
    for j in range(N):
        if SpaceMap[i][j] == 4:
            cell_end = SpaceMapCellId[i][j]
            break
    if cell_end != -1:
        break
# 타임머신 시작점: 위쪽 단면도에서 값이 2인 셀
for i in range(M):
    for j in range(M):
        if TimeWall[4][i][j] == 2:
            cell_start = TimeWallCellId[4][i][j]
            break
    if cell_start != -1:
        break

que = deque()
que.append(cell_start)
dist[cell_start] = 0

runs = 1
while True:
    # [G] 각 턴마다 진행되는 시간 이상 현상의 확장 처리
    for i in range(1, E + 1):
        if not events[i]["alive"]:
            continue
        if runs % events[i]["cycle"] != 0:
            continue
        nx = events[i]["xpos"]
        ny = events[i]["ypos"]
        steps = runs // events[i]["cycle"]
        # 방향에 따라 확장: 0(동), 1(남), 2(서), 3(북)
        if events[i]["direction"] == 0:
            ny += steps
        elif events[i]["direction"] == 1:
            nx += steps
        elif events[i]["direction"] == 2:
            ny -= steps
        else:
            nx -= steps
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            events[i]["alive"] = 0
            continue
        # 해당 셀이 장애물이면 더 이상 확장하지 않음
        if SpaceMap[nx][ny] != 0:
            events[i]["alive"] = 0
            continue
        idx = SpaceMapCellId[nx][ny]
        dist[idx] = INF

    # [H] BFS를 통한 경로 탐색
    next_cells = []
    size = len(que)
    for _ in range(size):
        idx = que.popleft()
        for d in range(4):
            idy = Graph[idx][d]
            if idy == -1:
                continue
            if dist[idy] != -1:
                continue
            dist[idy] = runs
            next_cells.append(idy)
    if not next_cells:
        break
    que.extend(next_cells)
    if dist[cell_end] != -1:
        break
    runs += 1

# [I] 결과 출력 (도달 불가능하면 -1)
if dist[cell_end] == -1 or dist[cell_end] >= INF:
    print(-1)
else:
    print(dist[cell_end])
