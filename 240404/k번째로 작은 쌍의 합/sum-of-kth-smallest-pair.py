import heapq
n,m,k = map(int,input().split())
arrn = []
arrm = []
d = map(int,input().split())
for i in d:
    heapq.heappush(arrn,i)
dd = map(int,input().split())
for j in dd:
    heapq.heappush(arrm,j)
pq = []
answer= k//2
for i in range(n):
    tmp = arrn[i]
    for j in range(m):
        tmp2= arrm[j] # 최솟값을 제거
        ans = tmp + tmp2
        heapq.heappush(pq,ans)
for i in range(k-1):
    heapq.heappop(pq)
print(pq[0])

"""
for i in range(n):
    for j in range(m):
        x = arrn[i]
        y = arrm[j]
        heapq.heappush(pq, x+y) 

#제일 높은 인덱스가 -pq의 k번째의 -이므로..

print(pq)
print(pq[k-1])
"""