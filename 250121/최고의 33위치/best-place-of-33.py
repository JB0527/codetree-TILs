n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def collect_golds(start_r,start_c,end_r,end_c):
    golds = 0
    for i in range(start_r,end_r+1):
        for j in range(start_c,end_c+1):
            golds += grid[i][j]
    return golds
# Write your code here!
max_gold = 0
for row in range(n):
    for col in range(n):
        # 3by3으로 벗어나는 경우 표시
        if row + 2 >= n or col +2 >= n:
            continue
        num_of_golds = collect_golds(row,col,row+2,col+2)    
        max_gold = max(max_gold,num_of_golds)
print(max_gold)