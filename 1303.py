
import sys

sys.stdin = open("1303.txt", "r")
# N,M= map(int, input().split())
N, M = map(int, input().split())


from collections import deque

grid = [list(row) for row in sys.stdin.read().split()]


dx = [[1, 0], [-1, 0], [0, -1], [0, 1]]
#visited를 전역변수로 두고 방문한 노드의 경우 넘어가도록 했어야했음!
#battle 함수에서  W 인지 B인지에 따라 그 값을 시작값으로 1조회하고 다음 노드방문하는 bfs함수 실행하게 하는데,
#방문처리가 안되어있어서 bfs 실행시킴. 그래서 이미 방문한 애인데 시작해서 1 카운트 함!!
visited = [[False] * (N) for _ in range(N)]
print('//////////////')
def bfs(x, y, color):
    print("x",x,"y:",y,"color",color)
    # 현재 병사의 수
    count = 1
   

    row = len(grid)
    # 인덱스 0이 살짝 헷갈림
    col = len(grid[0])
    q = deque()
    #튜플은 바로 추가 안됨 append로 넣어야함
    q.append((x, y))

    # 첫 시작 방문
    visited[x][y] = True

    while q:
        # 방문할 곳
        cur_x, cur_y = q.popleft()
        # print("cur_x", cur_x ,"cur_y",cur_y)

        for i in range(4):
            next_x = cur_x + dx[i][0]
            next_y = cur_y + dx[i][1]
    
            # print("next_x:", next_x)
            # print("next_y:", next_y)
            # w 가 w면 몇개인지 세야함. 배열에 저장해놔야함
            # b가 b면 몇개인지 기록해야함. 배열에 저장해놔야함
            if (
                next_x >= 0
                and next_x < row
                and next_y >= 0
                and next_y < col
                and visited[next_x][next_y] == False
                and grid[next_x][next_y] == color  # 각 색을 어떻게 저장하나 했더니 color를 확인하는구나.
            ):
            
                # 방문 기록 및 다음방문 저장
                q.append((next_x, next_y))
                # print("q안:",q)
                visited[next_x][next_y] = True
                # print("visited:", visited)
                # print("count:",count)
                count += 1 
                # print("count:",count)
    return count   # 1을 더하는 이유가 뭐지? #맨처음 시작 1을 더하는건가?????


# 이제 각 색의 값을 제곱해서 더해야함

def battle(grid, N, M):
    W_answer = 0
    B_answer = 0
    w= []
    b = []

    # print("포문visited:",visited)
    for row in range(N):
        # print("포문row:",row)
        for col in range(M):
            # print("포문row:",row)
            # print("포문col:",col)
            # print("포문visited[row][col]",visited[row][col])
            if visited[row][col] == False:
                # print("포문grid[row][col]")
                if grid[row][col] == "W":
                    # print("포문bfs(row,col,grid[row][col]):",bfs(row,col,grid[row][col]))
                    # print("포문grid[row][col]:",grid[row][col])
                    w.append(bfs(row,col,grid[row][col]) **2)
                    # W_answer =  sum(w)
                    W_answer += bfs(row,col,grid[row][col]) **2

                    

                    print("11111:",W_answer)
         
                    # W_answer += bfs(row,col,grid[row][col]) ** 2
                    print("wwwwwwwwwwwww:", sum(w))
                
                
                
                elif grid[row][col] == "B":
                    # print("포문bfs(row,col,grid[row][col]):",bfs(row,col,grid[row][col]))
                    print("포문grid[row][col]:",grid[row][col])
                    b.append(bfs(row,col,grid[row][col]) **2)
                    B_answer =sum(b)
                    
                    print("bbbbbbbbbb",sum(b))

           
             
                    # B_answer += bfs(row,col,grid[row][col]) ** 2
                 



battle(grid, N, M)
