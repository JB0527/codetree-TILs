n = int(input())

left,right = {},{}

for _ in range(n):
    x, l, r = tuple(input().split())
    left[x] = l
    right[x] = r

# Write your code here!
def pre_order(x):
    if x == '.':
        return
    print(x,end = "")
    pre_order(left[x])
    pre_order(right[x])

def in_order(x):
    if x == '.':
        return
    in_order(left[x])
    print(x,end = "")
    in_order(right[x])

def post_order(x):
    if x == '.':
        return
    post_order(left[x])
    post_order(right[x])
    print(x,end = "")

pre_order("A")
print()

in_order("A")
print()
post_order("A")
print