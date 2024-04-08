from sortedcontainers import SortedSet

n,q = map(int,input().split())
pos = list(map(int,input().split()))
edges = [list(map(int,input().split())) for _ in range(q)]
#nums = SortedSet()

# 사용되는 모든 번호를 treeset에 넣어줍니다.
#for v1 in pos:
#    nums.add(v1)

# treeset에서 정점을 작은 번호부터 뽑으면서
# 각 정점별로 1번부터 순서대로 매칭하여
# 그 결과를 hashmap에 넣어줍니다.
start = pos[0]
end = pos[-1]
mapper = dict()
cnt = 1
for i in range(start,end+1):
    mapper[i] = cnt
    if i in pos:
        cnt +=1

#print(mapper)

for v1,v2 in edges:
    print(mapper[v2] - mapper[v1]+1)