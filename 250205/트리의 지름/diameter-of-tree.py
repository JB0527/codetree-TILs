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