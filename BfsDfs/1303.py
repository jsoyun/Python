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

def bfs(x, y, color):
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

        for i in range(4):
            next_x = cur_x + dx[i][0]
            next_y = cur_y + dx[i][1]
    
        
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
             
                visited[next_x][next_y] = True
           
                count += 1 
    return count   # count 1 로 하는 이유는 next없어도 처음 방문했을 때  1개니까. 

def battle(grid, N, M):
    W_answer = 0
    B_answer = 0
    w= []
    b = []

    for row in range(N):
        for col in range(M):
            if visited[row][col] == False:
                if grid[row][col] == "W":
                    w.append(bfs(row,col,grid[row][col]) **2)
                elif grid[row][col] == "B":
                    b.append(bfs(row,col,grid[row][col]) **2)

    print(sum(w), sum(b))
             

battle(grid, N, M)
