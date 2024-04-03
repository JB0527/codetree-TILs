import heapq

n = int(input())
pq=[]
for i in range(n):
    elem = int(input())
    if elem != 0:
        heapq.heappush(pq, elem) # priority queue에 넣어줍니다.
    elif elem == 0 and bool(pq) == False:
        print(0)
    else:
        minnum= heapq.heappop(pq)
        print(minnum)   # 최솟값을 출력합니다.