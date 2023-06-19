
import sys
sys.stdin = open('1260.txt','r')
input = sys.stdin.readline
# N,M ,V = int(input())
N,M ,V = map(int, input().split()) #첫째줄 변수값들
#이후는 값들은 그래프를 형성하는 값임
graph = [[] for i in range(N+1)] 

for _ in range(M):
    node_left, node_right = map(int, input().split())

   #인풋값이 1번 노드와 2번노드 연결 - 이 뜻이었다!!
    graph[node_left].append(node_right)
    graph[node_right].append(node_left)


for node in graph:
    #작은 값부터 탐색하려고 sort함
    node.sort()

def DFS(graph,V, visited = [] ): #root시작값 넣기, visited 타입은 배열이다.

    visited.append(V) #root계속 추가해줘야햠 재귀함수로 도니까
    for i in graph[V]: #재귀함수이므로 graph전체가 아닌 그 루트배열까지의 값들을 탐색
        
        if i not in visited:
  
            DFS(graph ,i, visited ) #배열 visited에다가 계속 추가됨
    return visited

print( *DFS(graph,V)) # *붙이니까 배열에서 값들만 나옴



from collections import deque

visited2 = [False] *(N+1) #N+1개니까 인덱스 N까지 생성됨

def Bfs(V):

    queue = deque([V]) 
 
    visited2[V] = True  #첫 방문 True
    #for문 전체 돌기 전에 하나씩 꺼내는 것은 그래프와 상관없이 큐가 빌때 까지~!~!~!~!~!~!
    while queue:
        cur_node = queue.popleft() #방문예정인 애에서 뽑아서
        print(cur_node, end=' ')
     
        # for node in range(1,N+1): #안됨
        for node in graph[cur_node]: #그래프에서 현재노드 인덱스에 연결된 노드를 방문해야함!!!

            if not visited2[node]: #반약에 node값을 방문하지 않았고 V와 연결이 되어있으며ㅕㄴ
                queue.append(node)# 방문예정 추가
                visited2[node] = True


Bfs(V)









