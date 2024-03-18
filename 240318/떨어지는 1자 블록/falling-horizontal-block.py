n, m ,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

for j in range(n-1):
    for i in range(m-1):
        if arr[j][k+i-1] == 0:
            True
        else:
            arr[j-1][k+i-1] = 1
            tmp = j-1
            break
if tmp == True:
    for i in range(k-1, k+m-1):
        arr[tmp][i] = 1
else:
    tmp = n-1
    for i in range(k-1, k+m-1):
        arr[tmp][i] = 1
        
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print().rstrip()