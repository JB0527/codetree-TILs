N, K, B = map(int, input().split())
arr  = [0]*(N+1)
prefix_sum = [0]*(N+1)

# Write your code here!
for i in range(B):
    x = int(input())
    arr[x]= 1
# 지워야하는 곳에 1을 넣고 업데이트를 하는게 맞음 ㅇㅇ    
prefix_sum[0] = 0
for i in range(1,N+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

#합찾기.. 연속하는 양만 해야하므로 k를 빼줌 그러면 추가해줘야하는 값만 나옴
min_value = 0
for i in range(1,N-k+2):
    min_value = min(prefix_sum[i+k-1]-prefix_sum[i],min_value)
print(min_value)