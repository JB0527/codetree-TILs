import collections

n, t = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(2)]
sol = collections.deque()
for i in arr:
    for j in i:
        sol.append(j)

for i in range(t):
    A = sol.pop()
    sol.appendleft(A)

answer1 =[]
answer2 =[] 
for idx,value in enumerate(sol):
    if idx <= n-1:
        answer1.append(value)
    else:
        answer2.append(value)
print(*answer1)
print(*answer2)