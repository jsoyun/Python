#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 전투 bfs, dfs문제
# 이 문제는 방문, 조회해서 푸는 문제구나.
# bfs로 풀면 될듯. dfs
# 일단 bfs 코드
# N = 5
# M =5
import sys

sys.stdin = open("1303.txt", "r")
# N,M= map(int, input().split())
N, M = map(int, input().split())
print("N:", N)
print("M:", M)

from collections import deque

grid = [list(row) for row in sys.stdin.read().split()]
w_number = 0
b_number = 0


def battle(x, y, color):
    # 현재 병사의 수
    count = 0
    visited = [[False] * (N) for _ in range(N)]

    row = len(grid)
    # 인덱스 0이 살짝 헷갈림
    col = len(grid[0])

    dx = [[1, 0], [-1, 0], [0, -1], [0, 1]]

    # f, s = dx[0]
    # print(f)
    # print(s)

    # 다음 방문할 곳
    # if grid[0][0] == "w":
    #     w_number = 1
    # else:
    #     b_number = 1

    q = deque()
    q.append((0, 0))

    # 첫 시작 방문
    visited[0][0] = True

    while q:
        # 방문할 곳
        cur_x, cur_y = q.popleft()
        print("cur_x", cur_x)
        print("cur_y", cur_y)

        for i in range(4):
            next_x = cur_x + dx[i][0]
            next_y = cur_y + dx[i][1]
            print("dx[i][0]:", dx[i][0])
            print("dx[0][i]:", dx[i][1])
            print("next_x:", next_x)
            print("next_y:", next_y)
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
                # print("grid[next_x][next_y]:", grid[next_x][next_y])
                # if grid[next_x][next_y] == "W":
                #     w_number += 1
                #     print("")

                #     # if next_x == 0 or next_y == 0 or grid[next_x][next_y] == 'B'
                # elif grid[next_x][next_y] == "B":
                #     b_number += 1

                # 방문 기록 및 다음방문 저장
                q.append((next_x, next_y))
                visited[next_x][next_y] = True

                print("visited:", visited)
                count += 1
    return count + 1  # 1을 더하는 이유가 뭐지? #맨처음 시작 1을 더하는건가?????


# 이제 각 색의 값을 제곱해서 더해야함

# if grid[next_x][next_y] == "W":
#     w_number += 1
#     print("")

#     # if next_x == 0 or next_y == 0 or grid[next_x][next_y] == 'B'
# elif grid[next_x][next_y] == "B":
#     b_number += 1


print("bfs::", battle(grid))

# grid = [ [-1]* (N) for _ in range(M)]
# print("grid:",grid)

# from collections import deque
# def bfs():
#     q = deque()
#     q.append((0,0))
