# 한 노드를 나타내는 구현체 입니다.
class Node:
    def __init__(self, data):
        # 문자열을 값으로 가집니다.
        self.data = data
        self.prev = None
        self.next = None

# 두 노드를 연결해줍니다.
def connect(s, e):
    if s is not None:
        s.next = e
    if e is not None:
        e.prev = s

# target 뒤에 s를 삽입합니다.
def insertNext(target, s):
    connect(s, target.next)
    connect(target, s)

# target 앞에 s를 삽입합니다.
def insertPrev(target, s):
    connect(target.prev, s)
    connect(s, target)

# target의 이전 노드, target, target의 다음 노드의 값을 출력합니다.
def printNode(target):
    n = "(Null)"

    # 이전 노드가 존재하지 않는다면, Null을 출력합니다.
    # 아니라면, 이전 노드의 값을 출력합니다.
    if target.prev is None:
        print(n, end=" ")
    else:
        print(target.prev.data, end=" ")

    # target의 값을 출력합니다.
    print(target.data, end=" ")

    # 다음 노드가 존재하지 않는다면, Null을 출력합니다.
    if target.next is None:
        print(n)
    else:
        print(target.next.data)

# 맨 처음 문자열을 입력 받습니다.
sInit = input().strip()

# 맨 처음 존재하는 노드를 만듭니다.
cur = Node(sInit)

# 연산의 개수를 입력 받습니다.
n = int(input())

for _ in range(n):
    arr = input().split()
    option = int(arr[0])

    # option이 1이라면, cur의 앞에 노드를 삽입합니다.
    if option == 1:
        # 삽입할 노드를 만듭니다.
        data = arr[1]
        target = Node(data)

        # cur의 앞에 삽입합니다.
        insertPrev(cur, target)

    # option이 2라면, cur의 뒤에 노드를 삽입합니다.
    if option == 2:
        # 삽입할 노드를 만듭니다.
        data = arr[1]
        target = Node(data)

        # cur의 뒤에 삽입합니다.
        insertNext(cur, target)

    if option == 3:
        # cur의 이전 노드가 존재한다면, cur을 cur의 이전 노드로 변경합니다.
        if cur.prev is not None:
            cur = cur.prev

    if option == 4:
        # cur의 다음 노드가 존재한다면, cur을 cur의 다음 노드로 변경합니다.
        if cur.next is not None:
            cur = cur.next

    # 매 연산이 진행될 때마다 cur의 값을 출력합니다.
    printNode(cur)