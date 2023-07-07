import sys
sys.stdin = open('input.txt','rt')
n = int(input())
list = list(map(int, input().split()))

#자릿수의 합
def digit_sum(x):
    sum = 0
    #나눠서 각 자리수 합 구하는 방법 1
    # while x >0:
        
    #     sum += x%10 #나머지
    #     x = x//10 #몫
    # return sum
    #string으로 바꿔서 그 자릿수 합 구하는 방법 2
    for i in str(x):
        sum += int(i)
    return sum
max = -2147000000
for i in list:
    sum_value = digit_sum(i)
    if max <sum_value:
        max = sum_value
        #그 값!!! 
        res = i 
print(res)


    