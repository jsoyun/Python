#top down #재귀
cost = [10,15,20,17,1]
memo = {}
def dp(n):
    if n ==0 and n==1:
        return 0
    if n not in memo:
        memo[n]= min(dp(n-1)+ cost[n-1], dp(n-2)+ cost[n-2])
    return memo[n]


#bottom up for문 반복
cost = [10,15,20,17,1]
# memo = {}
#초기화
memo = [-1]*n
def dp(n):
    # if n ==0 and n==1:
    #     return 0

    memo[0]= 0
    memo[1] = 0
    for k in range(2,n+1):
       
        memo[k]= min(memo[k-1] +cost(k-1), memo[k-2] +cost(k-2))
    return memo[n]
    # if n not in memo:
    #     memo[n]= min(dp(n-1)+ cost[n-1], dp(n-2)+ cost[n-2])
    # return memo[n]

