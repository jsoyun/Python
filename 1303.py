#!/usr/bin/env python
# -*- coding: utf-8 -*-
#전투 bfs, dfs문제
# 이 문제는 방문, 조회해서 푸는 문제구나. 
# bfs로 풀면 될듯. dfs
# 일단 bfs 코드 
# N = 5
# M =5
import sys
sys.stdin = open('1303.txt','r')
# N,M= map(int, input().split())
N,M= map(int, input().split())
print("N:",N)
print("M:",M)

from collections import deque
# first = list(input().split())
# rows = input.str.split('\n')
grid =  [list(row) for row in sys.stdin.read().split()]


print("grid:",grid)
print("grid[0][0]:",grid[0][0])
def battle(grid):
    ww = []
    w_number = 0    
    bb = []
    b_number = 0
    visited =[ [False]*(N) for _ in range(N)]
    print("visited:",visited)
    row = len(grid)
    #인덱스 0이 살짝 헷갈림
    col = len(grid[0])

    dx = [[1,0] ,[-1,0],[0,-1],[0,1]]

    # f, s = dx[0]
    # print(f)
    # print(s)

    #다음 방문할 곳
    if grid[0][0] == 'w':
         w_number = 1
    else:
        b_number = 1
    q= deque()
    q.append((0,0))
    print("qqqq:",q)
        #첫 시작 방문
    visited[0][0] = True
    print("q",q)
    while q:
        #방문할 곳
        cur_x,cur_y = q.popleft()
        print("cur_x",cur_x)
        print("cur_y",cur_y)
        for i in range(4):
            next_x = cur_x + dx[i][0]
            next_y = cur_y + dx[0][i]
            print("next_x:",next_x)
            print("next_y:",next_y)
            #w 가 w면 몇개인지 세야함. 배열에 저장해놔야함
            #b가 b면 몇개인지 기록해야함. 배열에 저장해놔야함
            if (next_x >= 0 and next_x < row and next_y >= 0 and next_y < col and visited[next_x][next_y] == False):
                if grid[next_x][next_y] == 'W'  :
                   
                    w_number += 1
                    # print("w_number:",w_number)
                   
                    # if next_x == 0 or next_y == 0 or grid[next_x][next_y] == 'B'
                elif grid[next_x][next_y] == 'B'  :
            
                   
                    b_number += 1
                q.append((next_x,next_y))
                visited[next_x][next_y] == True
                print("w_number,b_number:",w_number,b_number)
            return w_number,b_number
                # elif next_x ==0 or next_x == 0 
                



                #     w_number += 1
                # elif  grid[next_x][next_x] != 'W' or :
                #     ww.append(w_number)
                #     print("ww:",ww)
                # elif grid[next_x][next_x] == 'B':
                #     b_number += 1



    

        return
        #방문했다는걸 기록해야함.
        if x not in visited:
            visited
        #다음에 방문할 곳을 추가해야함!
        #동서남북으로 이동 next_q
        #x의 현위치를 어떻게 파악하지?
        #grid로! ㅎ
        # for r in
        #     next_q = x + dx[r]
        #     if x 
        # q.append()



print("bfs::",battle(grid))

# grid = [ [-1]* (N) for _ in range(M)]
# print("grid:",grid)

# from collections import deque
# def bfs():
#     q = deque()
#     q.append((0,0))


