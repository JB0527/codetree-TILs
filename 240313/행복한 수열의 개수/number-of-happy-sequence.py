from collections import defaultdict
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
"""
answer = 0
check = defaultdict
for row in arr:
    for i in row:
        check[i] += 1
    if check[?] >= m:
        answer += 1

for i in range(N):
    for j in range(N):
        check[arr[j][i]] += 1
    if check[?] >= m:
        answer += 1
print(answer)
"""
answer = 0
for row in arr:
    check = defaultdict(int)
    for i in row:
        check[i] += 1
        if check[i] >= M:
            answer += 1
            break

# Check happy sequences in columns
for i in range(N):
    check = defaultdict(int)
    for j in range(N):
        check[arr[j][i]] += 1
        if check[arr[j][i]] >= M:
            answer += 1
            break

print(answer)

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    bit = 0
    for j in range(N-M+1):
        for k in range(M):
            if arr[i][j] != arr[i][j+k]:
                break
        else:
            bit = 1
            break
    if bit == 1:
        result += 1

for i in range(N):
    bit_r = 0
    for j in range(N-M+1):
        for k in range(M):
            if arr[j][i] != arr[j+k][i]:
                break
        else:
            bit_r = 1
            break
    if bit_r == 1:
        result += 1

print(result)






"""
for row in arr:
    for i in row:
        if row[i:i+M].count(row[i]) == M:
            answer +=1
            break
for col in zip(*arr):
    for j in col:
        if col[i:i+M].count(col[j]) == M:
            answer +=1
            break
print(answer)"""