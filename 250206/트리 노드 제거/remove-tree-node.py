from collections import defaultdict,deque
n = int(input())
parent = list(map(int, input().split()))
remove_node = int(input())

tree = defaultdict(list)
# y는 자식 노드
for y in range(n):
    if parent[y] != -1:
        x = parent[y]
        tree[x].append(y)
    # if parent[y]



# print(tree)
# tree의 자식들도 다 지워야함..
q = deque()
q.append(remove_node)
while q:
    remove_nodes = q.popleft()
    # print(remove_nodes)
    tmplist = tree.pop(remove_nodes)
    # q에서 bfs로 찾듯이 이용하고 제거해야할 것들을 탐색 없으면 종료
    for node in tmplist:
        # 3,4 ,5 6, 밑에 딸린것들 다 제거해야함
        # 그래서 제거할 때 있으면 다 탐색해주고 탐색해서 있으면 걸러내는 작업추가
        # print(node)
        # 노드가 있으면 이걸 q에추가하고 제거
        if node in tree:
            # print(node)
            q.append(node)
            # print(tree.pop(node))
answer = 0
for tr in tree:
    for t in tree[tr]:
        if t != remove_node:
            answer += 1
print(answer)