#입력할 값은 문제에서 준다!
#알고리즘을 쓰는 것. 
#내가 원하는 형태로 데이터가 굴러가도록 틀을 먼저 짜놔야함

#그래프 구현
# 1번 통해서 바이러스 걸리게 되는 컴퓨터 수 구하시오
import sys
sys.stdin = open('2606.txt','r')
input = sys.stdin.readline
n = int(input()) #컴퓨터의 개수, 입력될
v = int(input()) #연결선 개수
#빈그래프 생성, n+1개의 빈 리스트로 구성된 graph생성
graph = [ [] for i in range(n+1)] #컴퓨터 1~n개까지
visited = [0]* (n+1) #방문한 노드 체크 visited리스트를 초기화 모두 0으로

for i in range(v): #그래프 생성   #입력받은 두 수를 정수로 변환해서 a,b,에 저장
    a,b = map(int, input().split()) 
    graph[a] += [b] #a 인덱스에 해당하는 리스트 
    graph[b] += [a] #양방향 

#DFS 알고리즘
def dfs(v):
    visited[v] =1 #방문 표시
    for nx in graph[v]: #v번 컴퓨터에 연결된 컴퓨터의 리스트
        if visited[nx] == 0: #방문이 안되어 있으면
            dfs(nx) 


dfs(1)
print(sum(visited)-1) #1번 컴퓨터 제외