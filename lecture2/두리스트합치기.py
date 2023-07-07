import sys
sys.stdin = open('input.txt','rt')
n = int(input())
a = list(map( int, input().split()))
m = int(input())
b = list(map( int, input().split()))

# c = [0]*(n+m)
c= []
print("c",c)
#p1, p2를 0으로 초기화
p1= p2 = 0

while p1 <n and p2 <m:
    if a[p1]  <= b[p2]:
        c.append(a[p1])
        print("a<b :c",c)
        p1 += 1
    else:
        c.append(b[p2])
        print("c",c)
        p2 +=1
if p1 <n:
    c = c+ a[p1:]
if p2 < m:
    c = c +b[p2:]
 


# for p1 in range(0,n):
#     print("p1:",p1)
#     for p2 in range(0,m):
#         print("p2:",p2)
#         if a[p1] <= b[p2]:
#             c[p1] = a[p1]
#             c[p2] =b[p2]
# print("c",c)






#sort로 풀었는데 sort로 하게 되면 시간복잡도 커진다. 위에 답지 있음
# print(n,List1)
# print(m,List2)

# for i in List2:
#     List1.append(i)
#     print("List1::",List1)
    
# List1.sort()

# for i in List1:

#     print(i , end = ' ')

