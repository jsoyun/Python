import sys
sys.stdin = open('input.txt','rt')
n = input()


#숫자 추출
# result = ''.join(c for c in n if c.isdigit())
res = 0
for i in n:

    if i.isdecimal():
        res = res * 10 + int(i)



k = res

check = [0]*(k+1)

cnt = 0
for i in range(1, k+1):
    if k % i == 0:  
        cnt += 1
print(k)
print(cnt)






