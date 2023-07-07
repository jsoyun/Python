import sys 
sys.stdin = open('input.txt','rt')
# a ,b = map(int, input().split())
#한번에 만들기
card= list(range(21))
#내가 만든거
# card = [0]*( 20 +1)
# print("card:",card)
# cnt = 0
# for i in range(1, 21):
#     cnt += 1
#     card[i] = cnt
# print("card:",card)


print("card:",card)
#인풋값을 10번 반복해서 가져옴
for _ in range(10):
    a ,b = map(int, input().split())
    for i in range((b-a+1)//2):
        card[a+i] , card[b-i] = card[b-i] ,card[a+i]
#card에서 0빼기
card.pop(0)
for x in card:
    print(x, end= ' ')
    
       
# print(a ,b)



# # a=5
# # a= a-1
# # b= 10

# # a=9
# # b= 13

# a= a-1
# print("a:",a)





