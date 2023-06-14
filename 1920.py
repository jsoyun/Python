# #이진탐색으로 숫자 찾자 
# #왼쪽, 오른쪽

# def findx(array, target):
#     left = 0
#     right = len(array) -1
#     mid = array[len(array) // 2]
#     if (target !== mid):
#         if(target > mid):
#             left = mid
#             right = len(array) -1 - mid
#         elif(tartget < mid):
#             right = mid
#             left = 0


# c = "1,2"
# print(list(map(int, c.split(',')))) #split은 문자열에만 된다. 배열을 하고 싶으면 join
# # print(list(map(int, c)))

import sys
sys.stdin = open('1920.txt','r')
input = sys.stdin.readline
N = int(input())
A= list( map ( int, input().split()))
M = int(input())
arr = list( map ( int, input().split()))
A.sort()	#순서대로 정렬
print(A	)

#이진탐색
for num in arr:  #num이 타겟값
    lt, rt = 0,  N-1
    isExist = False #찾음 여부
    #이분탐색 시작
    while lt <= rt:#반복문 멈춤 조건
        mid = (lt +rt)//2
        if A[mid]  == num:
            isExist = True #찾음
            print(1)
            break
        elif A[mid] < num:
            lt = num +1
        else:
            rt = num -1
    if not isExist:
        print(0)



