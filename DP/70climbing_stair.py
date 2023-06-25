#dp'
#계단 오른 횟수를 저장
#계단의 갯수 n
# n = int(input())
n = 3
#횟수 저장
#[] 빈배열을 반복해봤자 그대로임
d = [0] * (n+1)


def climbing_Stair(n):
    #bottomup : for (탑다운은 재귀쓰게됨)
    # 0,1 부터 시작함
   
    d[1] = 1
    print
    for n in range(2, n+1):
        d[n] = d[n-1] +1
    print("d:",d[n])

climbing_Stair(n)


