#BFS사용한 
from collections import deque

def numIslands(grid):
    number_of_islands = 0
    row = len(grid)
    colum = len(grid[0])
    print("colum",colum)
    print("row",row)
    # return
    #방문을 false로 초기화
    visited = [[False]*colum for _ in range(row)]
    print("visited",visited)

    def bfs(x,y):
        #주변확인 (x,y)
       # 상하좌우 순이다 
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        #방문했으면 참
        visited[x][y] = True
        queue = deque()
        queue.append((x,y))
        print("queue:",queue)
        while queue:
            cur_x, cur_y = queue.popleft()
            for i in range(4): #상하좌우
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if (next_x >=0 and next_x <row and  0 <= next_y <colum):
                    if grid[next_x][next_y] == '1' and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append((next_x,next_y))
    for i in range(row):
        for j in range(colum):
        
            if grid[i][j] == '1' and not visited[i][j]:
                bfs(i,j)
                number_of_islands += 1
    return number_of_islands

print( numIslands(grid = [
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1']

]))