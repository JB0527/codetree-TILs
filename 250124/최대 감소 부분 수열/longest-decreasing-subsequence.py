n = int(input())
m = list(map(int, input().split()))
dp = [[0] for _ in range(n)]

# Write your code here!
# 최대의 방법 다 찾기 브루트포스 vs arr을 뒤집어서 하나씩 올라가기..
#맨끝은 수열을 못만듦
dp[0][0] =m[0]
for i in range(n):
    curscore= m[i]
    for j in range(i+1,n):
        #print(j)
        if curscore > m[j]:
            curscore = m[j]
            dp[i].append(m[j])
        else: continue
print(len(max(dp)))