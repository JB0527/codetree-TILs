# 한 노드를 나타내는 클래스입니다.
class Node:
    def __init__(self, id):
        self.id = id
        self.prev = None
        self.next = None

# u 앞에 singleton을 삽입합니다.
def insertPrev(u, singleton):
    singleton.prev = u.prev
    singleton.next = u
    if singleton.prev is not None:
        singleton.prev.next = singleton
    if singleton.next is not None:
        singleton.next.prev = singleton

# u 뒤에 singleton을 삽입합니다.
def insertNext(u, singleton):
    singleton.prev = u
    singleton.next = u.next
    if singleton.prev is not None:
        singleton.prev.next = singleton
    if singleton.next is not None:
        singleton.next.prev = singleton

# 노드 u를 제거합니다.
def pop(u):
    if u.prev is not None:
        u.prev.next = u.next
    if u.next is not None:
        u.next.prev = u.prev
    u.prev = u.next = None

n = int(input())
q = int(input())

# N 개의 단일 노드를 생성합니다.
nodes = [None] + [Node(i) for i in range(1, n+1)]

# Q 개의 연산을 진행합니다.
for _ in range(q):
    inputs = list(map(int, input().split()))
    option = inputs[0]
    i = inputs[1]
    if option == 1:
        pop(nodes[i])
    elif option == 2:
        j = inputs[2]
        insertPrev(nodes[i], nodes[j])
    elif option == 3:
        j = inputs[2]
        insertNext(nodes[i], nodes[j])
    elif option == 4:
        print((0 if nodes[i].prev is None else nodes[i].prev.id), (0 if nodes[i].next is None else nodes[i].next.id))

# 연산을 마친 후 1번 부터 N번 노드까지의 다음 노드 번호를 차례대로 한 줄에 출력합니다.
print(' '.join(str(0 if nodes[i].next is None else nodes[i].next.id) for i in range(1, n+1)))