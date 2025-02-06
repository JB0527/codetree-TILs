from collections import defaultdict
n = int(input())
parent = list(map(int, input().split()))
remove_node = int(input())

tree = defaultdict(list)
# y는 자식 노드
for y in range(n):
    if parent[y] != -1:
        x = parent[y]
        tree[x].append(y)


answer = 0
for tr in tree:
    if tr != remove_node:
        for value in (tree[tr]):
            if value != remove_node:
                answer += 1
print(answer)