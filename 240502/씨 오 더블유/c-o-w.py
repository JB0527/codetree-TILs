n = int(input())
arr = list(input())
#print(arr)

L, R = [0] * n, [0] * n #c, w가 각각 몇 개 있는지
L[0] = (1 if arr[0] == 'C' else 0)
R[-1] = (1 if arr[-1] == 'W'else 0)
#초반부터 장난질하면 잘라버리기

for i in range(1, n):
    L[i] = L[i-1]
    if arr[i] == 'C':
        L[i] += 1
#이후에 다시나올수 있는 C의 경우의수를 고려하여 각 순서대로에서의 앞에것 C값과 W값을 누적합처럼 채워놓기
for i in range(n-2, -1, -1):
    R[i] = R[i+1]
    if arr[i] == 'W':
        R[i] += 1
#print(L, R)

#o의 갯수만큼 LR 가짓수 곱하기
cnt = 0
for i in range(1, n-1):
    if arr[i] == 'O':
        cnt += (L[i] * R[i])

print(cnt)