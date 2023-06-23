
#컴퓨터의 수
n = int(input())
#연결선의 수
edge = int(input())

#그래프 구현하기 
#그래프 초기화 1부터 n까지
graph = [ [] for i in range(n+1)]
visited = [0]*[n+1]
for i in range(v):
    a,b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
    



#구현한 그래프를 탐색한다. 





#1번 컴퓨터와 연결된 컴퓨터의 수