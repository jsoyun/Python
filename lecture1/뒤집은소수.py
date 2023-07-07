import sys
sys.stdin = open('input.txt','rt')
n = int(input())
list = list(map(int, input().split()))


#나누기로 뒤집기 ! 다른 방법으로 뒤집는거 없나?
def reverse(x):
    res = 0
    while x >0:
        t = x%10
        res = res * 10 + t
        x = x//10 #몫
    return res
def isPrime(x):
    if x ==1:
        return False
    for i in range(2, x//2+1):
        if x%i ==0:
            return False
    else:
        return True


for i in list:
    check = reverse(i)
    if isPrime(check):
        print(check, end=' ')
