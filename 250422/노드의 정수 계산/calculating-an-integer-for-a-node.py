n = int(input())
edges = [[] for _ in range(n+1)]


arr = [0]*(n+1)
dp = [0]*(n+1)
# Initialize arrays with n+1 size to match 1-based indexing

# Process input for nodes 2 to n
for i in range(2, n + 1):
    t, a, p = map(int, input().split())
    edges[p].append(i)

    arr[i] = a if t==1 else -a

def dfs(x):
    for y in edges[x]:
        dfs(y)
    

    

# Please write your code here.
