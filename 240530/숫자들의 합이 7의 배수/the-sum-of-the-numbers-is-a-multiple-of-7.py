n = int(input())
arr = [int(input()) for i in range(n)]

tmp = 0
for i,value in enumerate(arr):
    if  value % 7 == 0:
        tmp += 1
        arr.pop(i)

def finding(arr):
    answer = 0
    find = arr.pop()
    for j,value in enumerate(arr):
        if (find + j) % 7 == 0:
            answer += 2
            arr.pop(j)
    return answer
answers = 0
while len(arr) >= 1:
    answers += finding(arr)
#print(arr)
print(answers+tmp)