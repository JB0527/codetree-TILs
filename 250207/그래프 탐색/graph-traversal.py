n, m = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(m)]
edges = [[] for _ in range(n+1)]
visited = [False] *(n+1)


# Write your code here!
for x,y in arr:
    edges[x].append(y)
    edges[y].append(x)
ans = []
def traversal(x):
    global ans
    for y in edges[x]:
        if not visited[y]:
            visited[y] = True
            traversal(y)
            ans.append(1)

traversal(1)
if len(ans) != 0:
    print(len(ans)-1)
else:
    print(0)