n, m ,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

for j in range(n):
    for i in range(m):
        if arr[j][k+i-1] == 0:
            tmp = n-1
        elif arr[j][k+i-1] == 1:
            tmp = j-1
            break
        else:
            tmp = n-1
    else:
        continue 
    break 

for i in range(k, k+m):
    arr[tmp][i-1] = 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()