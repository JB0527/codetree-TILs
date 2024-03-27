N = int(input())
lists = list(map(int,input().split()))
#dp = [0 for _ in range(N)]
num = 0
answer = []
i = 0
for i in range(N):
    if lists[i] > num:
        num = lists[i]
        answer.append(lists[i])
        i+=1
        continue
    else:
        i+=1
        continue

print(len(answer))