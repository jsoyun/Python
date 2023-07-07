import sys
sys.stdin = open('input.txt','rt')
n = int(input())
list =list(map( int , input().split()))

#간단방식
sum = 0
cnt = 0
for x in list:

    if x ==1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)


#내가 푼 방식 
# score = [0]* (n)
# for i in range(n):

#     if i ==0:
#         if list[i] ==1:
#             score[i] =1
         
#         else:
#             score[i] =0
#     elif list[i] ==1:
#         if list[i-1] ==list[i]:
#             print("i",i)
#             print("list[i-1]",score[i-1])
#             score[i] =score[i-1]+1
#         else:
#             score[i] = 1
#     elif list[i] ==0: 
#         score[i] = 0
# print(sum(score))
# print(score)
