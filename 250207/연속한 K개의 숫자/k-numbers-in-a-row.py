N, K, B = map(int, input().split())
missing = [int(input()) for _ in range(B)]

# Write your code here!
prefix_sum = [0]*(N+1)

for i in range(1,N+1):
    if i not in missing:
        prefix_sum[i] += 1
        if prefix_sum[i-1] != 0:
            prefix_sum[i] += prefix_sum[i-1]
# print(prefix_sum)
max_value = 0
for i in range(N+1):
    for j in range(i+1,N+1):
        max_value = max(prefix_sum[j]+prefix_sum[i],max_value)
        # print(max_value)
print(K-max_value)