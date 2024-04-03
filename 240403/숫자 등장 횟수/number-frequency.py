n , m = map(int,input().split())
arrn = list(map(int,input().split()))
arrm = list(map(int,input().split()))

import collections

numorder = collections.defaultdict(int)

for i, num in enumerate(arrn):
    numorder[num] += 1

list = []
for tmp in arrm:
    list.append(numorder[tmp])

print(*list)