import heapq
n,m = map(int,input().split())
arr = list(map(int,input().split()))

pq = []
for elem in arr:
    heapq.heappush(pq, -elem)
for i in range(m):
    maxn = heapq.heappop(pq)
    heapq.heappush(pq,maxn+1)   # 최댓값을 제거


print(-pq[0])