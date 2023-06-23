#DFS로 푸는 법 답지


def canvisitAllRooms(rooms):
    visited = [False] * len(rooms) #방문안했으면 false

    def dfs(cur_v):
        # visited.append(cur_v)
        #
        visited[cur_v] = True 
        for next_v in rooms[cur_v]:
            #방문했는지 체크. 방문했으면 또 방문안한다
            if visited[next_v] == False:
                dfs(next_v)
    #첫번째 방 입장
    dfs(0)
    # 만약에 모든 visited가 true면 방문했으면 true
    return all(visited)
    # if len(visited) == len(rooms):
    #     return True
    # else:
    #     return False
 

# dfs('A')

rooms = [[1,3],[2,4],[0],[4],[],[3,4]]
print(canvisitAllRooms(rooms))


#BFS로 푸는 법 답지
# from collections import deque

# def Go(rooms):
#     #초기화
#     visited = [False] * len(rooms)
#     #시작 true
#     def bfs(v):

  

#         q = deque()

#         q.append(v)
#         visited[v] = True
  
#         while q:
#             cur_v = q.popleft()
#             for next_v in rooms[cur_v]:
#                 if visited[next_v] == False:
#                     q.append(next_v)
#                     visited[next_v] =True
         
            
#     bfs(0)
#     return all(visited)

# print(Go([[1],[2],[3],[]]))