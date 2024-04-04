"""
N, G = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(G)]
s = set() #이미 초대장을 받은 친구들
s.add(1)
ans = [1]
for i in range(G):
    num = arr[i][0]
    stmp = set(arr[i][1:])
    for k in ans:
        if k in stmp:
            stmp.remove(k)
            num -= 1
    if num <= 2 :
        for p in stmp:
            ans.append(p)
    arr[i][0] = len(stmp)
    arr[i][1:] = list(stmp)

for i in range(G):
    num = arr[i][0]
    stmp = set(arr[i][1:])
    for k in ans:
        if k in stmp:
            stmp.remove(k)
            num -= 1
    if num < 2 :
        for p in stmp:
            ans.append(p)
print(len(set(ans)))
"""
"""
from collections import deque

# 변수 선언 및 입력:
n, g = tuple(map(int, input().split()))

invited = [False] * n
# 각 그룹마다 초대장을 받지 못한 사람들을 관리해줍니다.
groups = [set() for _ in range(g)]
# 각 사람이 어떤 그룹에 속하는지를 관리해줍니다.
people_groups = [[] for _ in range(n)]

q = deque()
ans = 0

for i in range(g):
    nums = list(map(int, input().split()))[1:]
    for num in nums:
        num -= 1
        groups[i].add(num)
        people_groups[num].append(i)

q.append(0)
invited[0] = True
while q:
    x = q.popleft()
    ans += 1

    # x가 들어있는 그룹에서 x를 지웁니다.
    # hashset에는 그룹에서 초대받지 않은 인원만을 남깁니다.
    for g_num in people_groups[x]:
        # 해당 그룹에서 x를 지웁니다.
        groups[g_num].remove(x)
        # 초대받지 않은 인원이 한명밖에 없다면 초대합니다.
        if len(groups[g_num]) == 1:
            p_num = list(groups[g_num])[0]
            if not invited[p_num]:
                invited[p_num] = True
                q.append(p_num)

# 초대장을 받는 인원을 출력합니다.
print(ans)
"""
N, G = map(int, input().split())

groups = [list(map(int, input().split())) for _ in range(G)]

invited = {1}  # People who have already received an invitation
invited_list = [1]  # List to keep track of invited people

for group in groups:
    group_size = group[0]
    group_members = set(group[1:])
    for person in invited_list:
        if person in group_members:
            group_members.remove(person)
            group_size -= 1
    if group_size <= 2:
        invited |= group_members
        invited_list.extend(group_members)

# Second pass to check if any group still has fewer than 2 remaining invitations
for group in groups:
    group_size = group[0]
    group_members = set(group[1:])
    for person in invited_list:
        if person in group_members:
            group_members.remove(person)
            group_size -= 1
    if group_size < 2:
        invited |= group_members
        invited_list.extend(group_members)

print(len(invited))