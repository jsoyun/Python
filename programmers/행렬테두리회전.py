#위치를 바꿔줘야함 회전! 가운데를 제외하고 테두리를 하나의 사각형으로 조회

def solution(rows, columns, queries):
    #행렬만들기 전체 행렬부터 만들어야하니?
    #작은 행렬, 우리가 검토할!!
    answer = []
    #0부터 있다 쳐서 인덱스 그대로 써도 되었음
    matrix = [ [0 for i in range(rows +1 ) ] for j in range(columns+1) ]
    print("matrix:",matrix)
    num = 1

    #아 이게 전체 행렬을 만든 부분이구나!!!!
    #matrix에다가 하나 하나 담기
    for row in range(1, rows+1):
        print("row:",row)
        for column in range(1, columns+1):
            print("column:",column)
            matrix[row][column] = num
            # print("matrix[row][column]:",matrix[row][column])
            num += 1
            print("matrix[row][column]:",matrix[row][column])

    #주의할 것이 회전할 때 그 값이 달라질 때 방향이 틀려지네.
    #최소값은 처음 값이 최소값인데 이후에는 회전에 되어서 각 방향에서 최소값이 나올 수 있어서 비교하네
    for x1,y1,x2,y2 in queries:
        print("x1,y1,x2,y2:",x1,y1,x2,y2)
        tmp =matrix[x1][y1]
        mini = tmp
        print("tmp:",tmp)
        #왼쪽측면부터 최소값 찾기
        for k in range(x1,x2):
            next = matrix[k+1][y1] 
            print("next:",next)
            #기존꺼 , 그 다음꺼. 
            matrix[k][y1] = next
            mini = min( mini ,next   )
            print("next:",next)
            print("mini:",mini)
         #아래   
        for k in range(y1, y2):
            next = matrix[x2][k+1]
            matrix[x2][k]= next
            print("next:y",next)
            mini= min (mini, next)
            print("y측mini:",mini)
        #오른쪽 , 헷갈리는건 반대로 해야함!!
        for k in range(x2,x1,-1):
            next = matrix[k-1][y2]
            matrix[k][y2] = next
            mini = min(mini, next)
        #맨 위!
        for k in range(y2,y1,-1):
            next = matrix[x1][k-1]
            mini = min(mini, next)
        matrix[x1][y1+1] = tmp
        answer.append(mini)
    return answer


 

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))