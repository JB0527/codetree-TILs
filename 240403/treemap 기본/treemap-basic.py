from sortedcontainers import SortedDict
import collections

n = int(input())
sd = SortedDict(int)
#dic = collections.defaultdict(int)

list = [list(map(str,input().split())) for _ in range(n)]

for i in list:
    if i[0] == 'add':
        sd[i[1]] = i[2] 
    elif i[0] == 'find':
        if i[1] not in sd:
            print('None')
        else:
            print(sd[i[1]])
    elif i[0] == 'remove':
        sd.pop(i[1])
    elif i[0] == 'print_list':
        if len(sd) == 0:
            print('None')
        else:
            for k,v in sd.items():
    # 처음 나온 숫자라면 0을 출력합니다.
                if k not in sd:
                    print('None')
    # 나온 적이 있는 숫자라면, 빈도수를 출력해줍니다.
                else:
                    print(v, end=" ")   
        print()