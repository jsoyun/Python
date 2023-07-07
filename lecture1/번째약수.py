
import sys
sys.stdin = open("input.txt","rt")

N ,k =map( int, input().split())

def checkMeasure(N, k):
    measure = []
    for i in range(1 , N+1):
        if N% i ==0:
            measure.append(i)
            print("measure:",measure)
        

    if len(measure) -1 < k:
        return -1
    else:
        measure.sort()
        return measure[k-1]
    
print(checkMeasure(N, k))

