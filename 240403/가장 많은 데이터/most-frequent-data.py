n = int(input())
arr = [input() for _ in range(n)]

import collections
strorder = collections.defaultdict(int)

for t in arr:
    strorder[t] += 1

print(max(strorder.values()))