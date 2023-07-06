def solution(rows, columns, queries):
    matrix = [[0 for i in range(0,rows+1)] for j in range(0,columns+1)] 
    answer = []
    num = 1 
    for i in range(1,rows+1):
        for j in range(1,columns+1 ):
            matrix[i][j] = num
            num += 1
    for x1,y1,x2,y2 in queries:

        first = matrix[x1][y1]
        min_value = first

        for k in range(x1,x2):
            next = matrix[k+1][y1]
            matrix[k][y1] =next
            min_value = min(min_value , next)
        for k in range(y1, y2):
            next = matrix[x2][k+1]
            matrix[x2][k] = next
            min_value = min(min_value ,next)
        for k in range(x2, x1, -1):
            pre = matrix[k-1][y2]
            matrix[k][y2] = pre
            min_value = min(min_value,pre)
        for k in range(y2, y1, -1):
            pre = matrix[x1][k-1]
            matrix[x1][k] = pre
            min_value = min(min_value,pre)
        matrix[x1][y1+1]= first
        answer.append(min_value)
        
    return answer



rows = 6
columns =6
queries= [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

print(solution(rows, columns, queries))