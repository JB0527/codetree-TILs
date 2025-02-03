n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# Write your code here!
counts = 0
for i in range(n,0,-1):
    # print(coins[i-1])
    ans = k // coins[i-1]
    k -= ans*coins[i-1]
    counts += ans
print(counts)
