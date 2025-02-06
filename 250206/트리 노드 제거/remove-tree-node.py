from collections import defaultdict, deque

n = int(input())
parent = list(map(int, input().split()))
remove_node = int(input())

tree = defaultdict(list)
root = -1

# 트리 구성
for child in range(n):
    if parent[child] == -1:
        root = child  # 루트 노드 저장
    else:
        tree[parent[child]].append(child)
# BFS를 사용하여 삭제할 노드 및 그 자식 노드들 제거
q = deque([remove_node])
while q:
    node = q.popleft()
    if node in tree:
        q.extend(tree[node])  # 삭제할 노드의 자식들을 큐에 추가
        del tree[node]  # 해당 노드 삭제

# 리프 노드 개수 계산
def count_leaves(node):
    if node not in tree or len(tree[node]) == 0:
        return 1  # 리프 노드
    return sum(count_leaves(child) for child in tree[node])

# 루트가 삭제된 경우 0 출력
if remove_node == root:
    print(0)
else:
    print(count_leaves(root)-1)

"""from collections import defaultdict,deque
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



# tree의 자식들도 다 지워야함..
q = deque()
q.append(remove_node)
while q:
    remove_nodes = q.popleft()
    print(remove_nodes,"pk")
    print(tree)
    tmplist = tree.pop(remove_nodes)
    # q에서 bfs로 찾듯이 이용하고 제거해야할 것들을 탐색 없으면 종료
    for node in tmplist:
        # 3,4 ,5 6, 밑에 딸린것들 다 제거해야함
        # 그래서 제거할 때 있으면 다 탐색해주고 탐색해서 있으면 걸러내는 작업추가
        print(node)
        # 노드가 있으면 이걸 q에추가하고 제거
        if node in tree:
            print(node)
            q.append(node)
answer = 0
for tr in tree:
    print(tree[tr])
    for t in tree[tr]:
        if t != remove_node:
            answer += 1
print(answer)
"""