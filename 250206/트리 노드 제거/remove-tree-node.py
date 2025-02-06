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

# 삭제된 노드를 부모 리스트에서 제거
for key in list(tree.keys()):
    if remove_node in tree[key]:
        tree[key].remove(remove_node)

# 리프 노드 개수 계산
def count_leaves(node):
    if node not in tree or len(tree[node]) == 0:
        return 1  # 리프 노드
    return sum(count_leaves(child) for child in tree[node])

# 루트가 삭제된 경우 0 출력
if remove_node == root:
    print(0)
else:
    print(count_leaves(root))