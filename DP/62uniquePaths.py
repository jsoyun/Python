#완전탐색 DFS 재귀로 품
# def dfs(r,c):
#     if r == 2 and c ==6:
#         return 1
#     unique_paths = 0
#     if r+1 <3:
#         unique_paths += dfs(r+1,c)
#     if c+1 <7:
#         unique_paths += dfs(r, c+1)
#     return unique_paths 


# def dfs(r,c):
#     if r == 0 and c ==0:
#         return 1
#     unique_paths = 0
#     if r-1 >=0:
#         unique_paths += dfs(r-1,c) #한칸 위쪽의 unique paths 값
#         print("(r-1)unique_paths:",unique_paths)
#     if c-1 >=0:
#         unique_paths += dfs(r, c-1) #한칸 왼쪽의 unique paths값
#         print("(c-1)unique_paths:",unique_paths)
#     print("unique_paths:",unique_paths)
#     return unique_paths 


# dfs(2,6)

#재귀로 푼 위에 코드에서 중복있는지 확인!!
# 중복있음
#dp로 중복을 없애보자!!
#top down 시간 복잡도 mXn 이 되겠구나. 
#메모리에서 꺼내쓴다.




# #메모
# memo = {}
# # 딕셔너리 튜플 형태로 저장하는데 
# # 키가 (r,c)가 된다. 값은 경우의 수!
# #메모 
# def dfs(r,c):
#     print("r,c:",r,c)
#     if r == 0 and c ==0:
#         memo[(r,c)] =1
#         print("memo:",memo[(r,c)])
#         return memo[(r,c)]
#     unique_paths = 0
#     print("unique_paths:",unique_paths)
#     #메모리에 추가가 안되어있다면
#     if (r,c) not in memo:

#         if r-1 >=0:
#          unique_paths += dfs(r-1,c) 
#          print("(r-1)r,c:",r, c,"unique_paths:",unique_paths)
#         if c-1 >=0:
#          unique_paths += dfs(r, c-1) #한칸 왼쪽의 unique paths값
#         print("(c-1)r,c:",r, c,"unique_paths:",unique_paths)
#         memo[(r,c)]= unique_paths
#     # print("unique_paths:",unique_paths)
#     return memo[(r,c)] 
# # dfs(2,6)

#top down
#이중리스트로 구현할 수도 있다!!
def unique(m,n):
   memo = [[-1] * n for _ in range(m)]
   def dfs(r,c):
        if r ==0 and c==0:
            memo[r][c] = 1
            return memo[r][c]
        unique_paths = 0
        if memo[r][c] == -1:
            if r-1>= 0:
                unique_paths += dfs(r-1,c)
            if c-1 >= 0:
                unique_paths += dfs(r,c-1)
            memo[r][c] = unique_paths
        return memo[r][c]
   return dfs(m-1,n-1)
print(unique(3,7))

#Bottm-up
#
def uniquePaths(m,n):
    #초기화 전체를 -1로 설정
    memo = [[-1]*n for _ in range(m)]
    #0 경우의 수 1인 애들 초기화!!!
    for r in range(m):
        memo[r][0] =1
    for c in range(n):
        memo[0][c] =1
    for r in range(1,m): #1~m-1
        for c in range(1, n):
            memo[r][c] = memo[r-1][c]+  memo[r][c-1]
    return memo[m-1][n-1]

uniquePaths(3,7)
