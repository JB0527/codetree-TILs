from collections import defaultdict
N = int(input())
#board = [list(map(str, input().split())) for _ in range(N)]
board = [list(input()) for _ in range(N)]
min_move = -1 #없으면 -1뱉기
arr = defaultdict(tuple)

for i,row in enumerate(board):
    for j,num in enumerate(row):
        if num == 'S':
            start = (i,j)
        elif num == '.':
            pass
        elif num == 'E':
            end = (i,j)
        else:
            arr[int(num)] = (i,j)

length = len(arr)

def distance(list1,list2):
    x1, y1 = list1
    x2, y2 = list2
    return abs(x1-x2) + abs(y1-y2)

#arr의 배열중 3개선택 -> 이걸 재귀로?
for i in range(1,length):
    for j in range(i+1,length):
        for k in range(j+1,length):
            move=0
            direct = [start,arr[i],arr[j],arr[k],end]
            for idx in range(4):
                move += distance(direct[idx],direct[idx+1])

            if min_move == -1:
                min_move = move
                continue
            
            min_move = min(min_move,move)
print(min_move)