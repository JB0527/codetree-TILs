n = int(input())
arr = list(map(int,input().split()))

count = 0
for i in arr:
    arr.remove(i)
    for j in arr:
        arr.remove(j)
        for k in arr:
            arr.remove(k)
            if sum(i,j,k) == 0:
                count += 1
print(count)