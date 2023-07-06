
arr = []
def draw(x,y,cnt, num):
    #num이 시작값인 듯
    #cnt는 뭐지?
    print("x:",x)
    print("y:",y)

    if cnt < 1:
        return
    number = num
    for i in range(cnt):
        arr[y+i][x] = number
        
        print("arr:",)
        print("number:",number)
        number += 1
    for i in range (1, cnt):
        arr[y+cnt -1][x+i] = number
        number += 1
    for i in range(1, cnt - 1):
        arr[y +cnt -1 -i][x + cnt -1 -i] = number
        number += 1
    print("number:::",number)
    #이렇게 해결을 했구나..
    draw( x +1 , y + 2, cnt -3 , number)
def solution(n):
    global arr
    arr = [[0]* n for _ in range(n)]
    draw(0,0,n,1)

    answer = []
    for i in range(n):
        for j in range(i+1):
            answer.append(arr[i][j])
    return answer

print(solution(10))

# n=10
# def make(n):
#     start = 1

#     example =   [[0] *x for x in range(1, n+1)] 
#     visited =[[0] *x for x in range(1, n+1)] 
#     print("example:",example)
#     #첫번째 줄

#     def bfs(start,firstLeft,firstRight):
#         #왼쪽 줄
        

#         for i in range(firstLeft, n):
#             example[i][firstRight] = i+1
#             visited [i][firstRight] = 1
#         #마지막 줄 채우기
#         for x in range(1, n):
#             print("x:",x)
#             print("n:",n)
#             print("n+x+1::",n+x+1)
#             example[n-1][x] =n+x
#             visited [n-1][x] = 1
#         example[n-1][0] =n

#         end = example[n-1][n-1]

#         #오른쪽 줄
#         for x in range(n-2, 0, -1):
#             end += 1
#             example[x][x] = end
#             visited[x][x] =1

#     if visited != 1:
        
       
#         bfs(start +1 ,firstLeft,firstRight)
# #     for i in range(n):
# #         example[i][0] = i+1
# #         visited [i][0] = 1
# #     #마지막 줄 채우기
# #     for x in range(1, n):
# #         print("x:",x)
# #         print("n:",n)
# #         print("n+x+1::",n+x+1)
        
        
# #         example[n-1][x] =n+x
# #         visited [n-1][x] = 1
# #     example[n-1][0] =n

# #     end = example[n-1][n-1]

# #   #오른쪽 줄
# #     for x in range(n-2, 0, -1):
# #         end += 1
# #         example[x][x] = end
# #         visited[x][x] =1
    
# #     lastValue = 0




#     # topNext = example[1][1] +1
#     # for x in range(2, n-1):
#     #     example[x][1] =topNext
#     #     topNext += 1
#     # leftNext= example[n-2][1]
#     # for x in range(1,n-2):
#     #     example[n-2][x] = leftNext
#     #     leftNext +=1
    



#     print("example:",example)
#     print("visited:",visited)



# print(make(n))