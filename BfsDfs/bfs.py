#고냥 외워라

from collections import deque

def bfs(graph, start_v):
    visited = [start_v]
    queue = deque(start_v) #큐료 시작담기
    while queue: #큐가 비어있을 때까지
        cur_v = queue.popleft() #큐에서 빠진것 들어감
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(V)
                queue.append(v)
    return visited



bfs(graph, 'A')