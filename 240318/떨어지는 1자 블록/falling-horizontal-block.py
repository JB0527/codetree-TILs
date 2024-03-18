n, m ,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

for j in range(n-1):
    for i in range(m-1):
        if arr[j][k+i-1] == 0:
            True
        elif arr[j][k+i-1] == 1:
            tmp = j-1
            break
        else:
            tmp = n-1
            
for i in range(k-1, k+m-1):
    arr[tmp][i] = 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()