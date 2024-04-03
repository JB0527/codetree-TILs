from sortedcontainers import SortedSet

n, m = map(int,input().split())
grid = [tuple(map(int,input().split())) for _ in range(n)]
query = [tuple(map(int,input().split())) for _ in range(m)]

s = SortedSet(grid)
#set2 = SortedSet(query)

for i in query:
    if s.bisect_right(i) != len(s):
        ans = s[s.bisect_left(i)]
        x,y = ans
        print(x,y)
    if s.bisect_right(i) == len(s):
        x,y = -1,-1
        print(x,y)
#    if s.bisect_right(i)