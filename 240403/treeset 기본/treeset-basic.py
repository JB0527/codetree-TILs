from sortedcontainers import SortedSet

s = SortedSet()
n = int(input())
arr = list(input().split() for _ in range(n))
for num,i in enumerate(arr):
    if i[0] != 'largest' and i[0] != 'smallest':
        arr[num][1] = int(arr[num][1])
    

for i in arr:
    if i[0] == 'add':
        s.add(i[1]) 

    elif i[0] == 'find':
        if i[1] not in s:
            print('false')
        else:
            print('true')
    elif i[0] == 'remove':
        s.remove(i[1])
    elif i[0] == 'lower_bound':
        if s.bisect_left(i[1]) == len(s):
            print('None')
        else:
            print(s[s.bisect_left(i[1])])
    elif i[0] == 'upper_bound':
        if s.bisect_right(i[1]) == len(s):
            print('None')
        else:
            print(s[s.bisect_right(i[1])])
    elif i[0] == 'largest':
        if bool(s) == False:
            print('None')
        else:
            print(s[-1])
    elif i[0] == 'smallest':
        if bool(s) == False:
            print('None')
        else:       
            print(s[0])