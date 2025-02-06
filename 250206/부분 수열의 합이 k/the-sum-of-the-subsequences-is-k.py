n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!

prefix_sum = [0]*(n+1)
# prefix_sum[i] = arr[i] 
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + arr[i]

ans = 0
for i in range(n+1):
    for j in range(i,n+1):
        if k == (prefix_sum[j]-prefix_sum[i]):
            ans +=1
print(ans)