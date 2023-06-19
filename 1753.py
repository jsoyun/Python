#최단경로 다익스트라 알고리즘

import sys
sys.stdin = open('1920.txt','r')
input = sys.stdin.readline
sys.setrecursionlimit(10**6) #재귀호출의 최대깊이를 설정하는 코드입니다. 

import heapq 

n, m = map(int, input().split())
k = int(input())
INF = int(1e9)
graph = [[]* (n+1) for _ in range(n+1)]

# 최댄거리 테이블을 모두 무한으로 초기화
distance = [INF]* (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    print( "그래프a",graph[a])
    graph[a].append((b,c))
    print(  '그래프aaa', graph[a].append((b,c)))

def dijkstra(start):
    q = []
# 함수는 heapq 모듈의 heappush 함수를 사용하여 데이터를 우선순위 큐에 삽입하는 것입니다. 이 함수는 최소 힙의 특성을 유지하며 데이터를 삽입하므로, 삽입된 데이터들은 우선순위에 따라 정렬되어 있게 됩니다.
    heapq.heappush(q,(0,start))
    distance[start] =0
    while q: #우선순위 큐 q가 비어있지 않은 동안 반복합
        #추출된 노드까지의 최단거리
        #현재 처리중인 노드
        #dist, now = heapq.heappop(q)를 통해 최소 힙의 특성에 따라 가장 작은 요소인 (dist, now)가 추출되
        dist, now = heapq.heappop(q) 
        print("q",q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[i]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))


# 다익스트라 알고리즘을 수행
dijkstra(k)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])