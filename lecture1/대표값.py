import sys
sys.stdin = open('input.txt','rt')
N = int(input())
List = list(map( int, input().split()))

#평균값 구하기 round가 소수점한자리까지 구한다. 
ave = round(sum(List)/N)
min = 2147000000
#인덱스와 값을 다 가져오기!!!
for idx , value in enumerate(List):
    #절대값!!abs()
    tmp = abs(ave-value)
    if tmp <min:
        min = tmp
        #점수 저장
        score = value
        # 맨 처음 값을 1이라고 시작해서!!
        res = idx +1
    elif tmp == min:
        if value> score:
            score = value
            res = idx+1

print(ave, res)
