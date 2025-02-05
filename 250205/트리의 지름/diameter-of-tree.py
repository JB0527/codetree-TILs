import sys
from collections import deque

# sys.setrecursionlimit(100000)

n = int(input())
edges = [[] for _ in range(n + 1)]

# 그래프 입력 받기
for _ in range(n - 1):
    x, y, score = map(int, input().split())
    edges[x].append((y, score))
    edges[y].append((x, score))

# BFS 함수
def bfs(start):
    visited = [False] * (n + 1)
    total = [0] * (n + 1)
    
    queue = deque([start])
    visited[start] = True
    far_vertex = start
    far_score = 0

    while queue:
        x = queue.popleft()
        for y, score in edges[x]:
            if not visited[y]:
                visited[y] = True
                total[y] = total[x] + score
                queue.append(y)
                
                # 가장 먼 정점 갱신
                if total[y] > far_score:
                    far_score = total[y]
                    far_vertex = y

    return far_vertex, far_score

# 1번 정점으로부터 가장 먼 정점 찾기
f, _ = bfs(1)

# f로부터 가장 먼 정점까지의 거리 찾기
_, scores = bfs(f)

# 결과 출력
print(scores)

"""
import sys
sys.setrecursionlimit(100000)
from collections import deque
n = int(input())
edges = [[] for _ in range(n + 1)]
#dfs로찾아야함 스코어비교해야해서
# y값이 정해짐

visited = [False] * (n+1)

total = [0] *( n+1) # 각 y->x로 향할때 값

# Write your code here!
for _ in range(n-1):
    x,y,score= tuple(map(int, input().split()))
    edges[x].append((y,score))
    edges[y].append((x,score))
# print(edges)
def dfs(x,total_score):
    for y,score in edges[x]:
        if not visited[y]:
            visited[y] = True
            total[y] = total_score+score
            dfs(y,total_score+score)

def find_largest_vertex(x):
    #초기화
    for i in range(n+1):
        visited[i] = False
        total[i]=0
    #dfs 진행
    visited[x] = True
    total[x] = 0
    dfs(x,0)
    
    #bfs로하는거나마찬가지
    far_score = -1
    far_vertx = -1
    for i in range(1, n + 1):
        if total[i] > far_score:
            far_score = total[i]
            far_vertx = i

    return far_vertx,far_score
        
# 1번 정점으로부터 찾기시작

f,_ = find_largest_vertex(1)

_,scores = find_largest_vertex(f)
print(scores)
"""