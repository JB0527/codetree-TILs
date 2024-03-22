n = int(input())

def fibonachi(n):
    prev = 0
    cur = 1
    for i in range(n):
        cur = prev + cur
    return print(cur)
fibonachi(n)