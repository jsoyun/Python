import sys
sys.stdin = open('input.txt','rt')
N , M = map( int, input().split())
print(N , M)

a = []
for i in range(1, N+1):
    print("i",i)
    for j in range(1, M+1):
        print("j",j)
        a.append(i+j)
        print("a:",a)

a.sort()
print(a)
#중복되는 갯수 많은거 어떻게 구하지?

