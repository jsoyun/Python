#dp문제임 dp로 수정하기
# 대한님코드 참조

import sys
sys.stdin = open('2748.txt','r')

n = int(input())
#앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
#n번째
d = [0]* (n+1)
print("d:",d)

#bottomtotop?인듯 base case먼저 제시
#0,1로 시작, 1번째 1  
d[1] =1
#반복문은 2번째부터 시작. 
for i in range(2, n+1): #2~n까지
    d[i] = d[i-1]+ d[i-2]
    print(d[n])

#혼자 큐로 품. 잘했는데 백준에서 돌리면 런타임 에러난다요~~
# import sys
# sys.stdin = open('2748.txt','r')
# input = sys.stdin.readline
# n = int(input())

# #피보나치 문제 큐로 풀지 말고 dp로 수정하기

# from collections import deque

# def Fcheck(k):
    
#     queue = deque()
#     queue.append(0)
#     queue.append(1)
    
#     n = 1


#     while n <k:
#         # Fn = len(queue)-1
      
#         Fn = queue[0] + queue[1]

#         queue.append(Fn)
#         n += 1 
#         queue.popleft()

    
       
#     print(Fn)
        

    
# Fcheck(n)


# # Fcheck(10)
