#bfs 구현
#정점 번호가 작은 것을 먼저 방문
# 왼쪽 오른쪽 비교했을 때 작은 것을 먼저 방문!

#큐
# import sys
# sys.stdin = open('1920.txt','r')
# input = sys.stdin.readline


import sys
sys.stdin = open('1260.txt','r')
input = sys.stdin.readline

N , M,start_v  = list(map(int, input().split()))
# M은??
# start_v = int(input())

Left,Right = list(map(int, input().split()))

print("N:",N ,"M:",M,"start_v:",start_v)
print("Left:",Left,"Right:",Right)

#정점, 간선, 시작
# N,M ,V

#방문하면 방문했다고 기록해야함!!
#

from collections import deque

def bfs(N,M, start_v ,Left,Right):
    queue = deque(start_v) #queue 방문할 애들
    visited = [] #방문한애들 추가
    cur_node = queue.popleft()
    print("queue:",queue)
    while queue:
     for i in N:
        if i not in visited:
       
         Left[i] = cur_node.left
         Right[i] = cur_node.right
         print("Left[i]",Left[i],"Right[i]", Right[i])
         if cur_node.left <cur_node.right:
            visited.append(cur_node.left)
            print("visited_left",visited)
            queue.append(cur_node.left)
         elif cur_node.left > cur_node.right:
            visited.append(cur_node.right)
            queue.append(cur_node.right)
            print("visited_right",visited)
        
     return visited
    


print(bfs(N,M, start_v ,Left,Right))
