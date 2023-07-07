import sys
sys.stdin = open('input.txt','rt')
N , K = map(int, input().split())
List = list(map(int, input().split()))
#set형식으로 만들어놓고
select = set()

for i in range(N):
    for j in range(i+1, N):
        for m in range(j+1, N):
            #거기다가 add추가!
            select.add(List[i]+ List[j]+ List[m])
            
#list로 다시 변환
select = list(select)
#큰수부터로 바꾸기
select.sort(reverse=True)
print(select[K-1])

