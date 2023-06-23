#bfs 사용한다. !
#1091. Shortest Path in Binary Matrix
from collections import deque

def shortestPath(grid):
    shortest_path = -1 
    row = len(grid)
    col = len(grid[0])
    queue = deque() 
    #grid의 x,y 와 경로 기록 : 1 
    queue.append((0,0,1))
    #방문 표시 안하면 무한루프를 돌 수 있다
    #기본 값을 False
    visited = [ [False] * col for _ in range(row)]
    
    delta = [
        #동서남북 [x,y] , 
        [1,0],[-1,0],[0,1],[0,-1],
        [-1,1],[1,1],[1,-1],[-1,-1]

    ]

    #우리는 방문할 때 true로 바꿔줄거임
    #일단 시작값
    visited[0][0] = True
    while queue:  
        cur_r, cur_c, cur_len = queue.popleft()
        print(cur_r, cur_c, cur_len)
        #마지막이면 -1이고 끝내기 
        if cur_r == row -1 and cur_c == col -1:
            print("shortest_pathshortest_path:",shortest_path)
            shortest_path = cur_len
            break
        #연결되어있는 vertx확인하기
        for dr, dc in delta:
            next_r = cur_r + dr
            next_c = cur_c + dc
      
            if next_r >= 0  and next_r < row and next_c >= 0  and next_c < col:
                if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:

                    queue.append([next_r, next_c,cur_len +1 ])
                    visited[next_r][next_c] = True
    print("shortest_path:",shortest_path)
    return shortest_path

#이부분이 이해가 안가면 그림을 그려보면 된다. 이것은 행렬을 나타낸것이다
grid = [[0,0,0],[1,1,0],[1,1,0]]   

print(shortestPath(grid))