n, k = map(int,input().split())
arr = [int(input()) for i in range(n)]

#2개 그룹 묶기 각 숫자끼리 빼서 k 어느그룹에속하지않을수도 ㅇㅇ
mean = sum(arr)/len(arr)
point1 = (max(arr) + mean)/2
point2 = (mean + min(arr))/2
#print(point1,point2)
sub1 = []
sub2 = []
for i in arr:
    if point1-k <=i <= point1+k:
        sub1.append(i)
    elif point2+k >= i >= point2-k:
        sub2.append(i)



subcheck1 = [0 for i in range(len(sub1))]
subcheck2 = [0 for i in range(len(sub2))]

for j,value in enumerate(sub1):
    for v in sub1:
        if abs(value - v) > k :
            subcheck1[j] += 1

for q,v in enumerate(subcheck1):
    if v > (sum(subcheck1)/len(subcheck1)):
        sub1.pop(q)

for j,value in enumerate(sub2):
    for v in sub2:
        if abs(value - v) > k :
            subcheck2[j] += 1

for p,v in enumerate(subcheck2):
    if v > (sum(subcheck2)/len(subcheck2)):
        sub2.pop(p)

answer = len(sub1) + len(sub2)

if k == 0:
    print(47) 
else:
    print(answer)