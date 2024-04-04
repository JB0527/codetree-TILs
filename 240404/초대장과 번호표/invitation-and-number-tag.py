N, G = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(G)]
s = set() #이미 초대장을 받은 친구들
ans=[1]
for i in range(G):
    num = arr[i][0]
    stmp = set(arr[i][1:])
    for k in ans:
        if k in stmp:
            stmp.remove(k)
        if num <= 2 :
            for p in stmp:
                ans.append(p)
        #for k in ans:
         #   if num <= 2 and k in stmp
          #      ans.append(j)
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
#print(ans)
print(len(set(ans)))