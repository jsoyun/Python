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
def battle(grid, visited = []):
    visited =[ [-1]*(N) for _ in range(N)]
    print("visited:",visited)

    dx = [(1,0) ,(-1,0),(0,-1),(0,1)]
    # f, s = dx[0]
    # print(f)
    # print(s)

    #다음 방문할 곳
    q= deque(grid[0][0])
        #첫 시작 방문
    visited[0][0] = 1
    print("q",q)
    while q:
        #방문할 곳
        x = q.popleft()
        print("x",x)

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


