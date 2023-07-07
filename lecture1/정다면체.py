import sys
sys.stdin = open('input.txt','rt')
N , M = map( int, input().split())
cnt =[0]*(N+M+1)


for i in range(1, N+1):
    for j in range(1, M+1):
        
        cnt[i+j]+= 1
#최대값
max = -2147000000
for i in range(N+M+1):
    tmp = cnt[i]
    if max < tmp:
        max = tmp

#인덱스 값 출력
for i in range(N+M+1):
    if cnt[i] ==max:
        print(i,end=' ')


#cnt 배열이 있고 인덱스가 

