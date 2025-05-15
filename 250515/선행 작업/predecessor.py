from collections import deque
import sys

input = sys.stdin.readline

n= int(input())
edges = [[] for _ in range(n+1)]

indegree = [0]*(n+1)

workTime=[0]*(n+1)

dp = [0]*(n+1)

q= deque()

for i in range(1,n+1):
    # 시간, 개수, 작업번호
    workTime[i],_,*nums= map(int,input().split())

    for x in nums:
        edges[x].append(i)
        indegree[i] += 1

for i in range(1,n+1):
    if not indegree[i]:
        q.append(i)
        dp[i] = workTime[i] # 초기조건으로 i번째작업엔 해당시간소요로 비교해서 사용
while q:
    x = q.popleft()

    for y in edges[x]:

        dp[y] = max(dp[y],dp[x]+workTime[y])

        indegree[y] -=1
        if not indegree[y]:
            q.append(y)
ans = 0
for i in range(1,n+1):
    ans = max(ans,dp[i])

print(ans)