import sys
sys.stdin = open('2748.txt','r')
input = sys.stdin.readline
n = int(input())

from collections import deque

def Fcheck(k):
    
    queue = deque()
    queue.append(0)
    queue.append(1)
    
    n = 1


    while n <k:
        # Fn = len(queue)-1
      
        Fn = queue[0] + queue[1]

        queue.append(Fn)
        n += 1 
        queue.popleft()

    
       
    print(Fn)
        

    
Fcheck(n)


# Fcheck(10)
