import sys 
sys.stdin = open('input.txt','rt')

n = int(input())

# N, s, e, k = map ( int, input().split())
# list = list(map ( int, input().split()))


for i in range(n):
    N, s, e, k = map ( int, input().split())
    a = list(map ( int, input().split()))
    a =a[s-1:e]
    a.sort()
    
    print("#%d %d" %(i, a[k-1]))


# cnt = 0
# def checkKnum(s,e,k):
    

#     x = []
#     for i in range(s-1 , e):
#         x.append(list[i])
#         x.sort()
     
#     print(f'#{cnt}', x[k-1])

# for i in range(2):
#     cnt += 1
#     checkKnum(s,e,k)
# print(checkKnum(s,e,k))


