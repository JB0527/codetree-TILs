n = int(input())

import collections

dic = collections.defaultdict()

list = [list(map(str,input().split())) for _ in range(n)]

answer = []
for i in list:
    if i[0] == 'add':
        dic[i[1]] = i[2] 
    elif i[0] == 'find':
        if i[1] not in dic:
            answer.append('None')
        else:
            answer.append(dic[i[1]])
    elif i[0] == 'remove':
        dic.pop(i[1])

for ans in answer:
    print(ans)