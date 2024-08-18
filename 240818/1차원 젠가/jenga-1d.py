n = int(input())
block = [int(input()) for _ in range(n)]
s1,e1 = map(int,input().split())
s2,e2 = map(int,input().split())

answer = block[:s1-1] + block[e1:]
ans = answer[:s2-1] + answer[e2:]
print(len(ans))
for _ in ans:
    print(_)