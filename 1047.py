from collections import deque
import sys
sys.stdin = open('1047.txt','r')
input = sys.stdin.readline

N,K= list(map(int, input().split()) )
array = []
print(N,K,array)

for i in range(N):
    a = list(map(int, input().split()))
    print("a:",a)
    array.extend(a)

print(N , K )
print("array:",array)


# Array = deque(array)
# print("Array:",Array)

check = 0
number = []


for n in array:
    while K >= 0:
        if K == 0:
            break
        for n in array:
            print("n",n,"K-n:",K-n)
            number.append(K-n)
        print("number::",set(number))
        positive_numbers = [ num for num in number if num >0]
        print("pn",positive_numbers)
        print("min", min(positive_numbers))
        check += 1
        K = K - min(positive_numbers)

print("check:",check)
    



    
  
    

    
    # if K - n > 0:

        # min(K - array[n])
        # number.append(K-n)
        # print("K - n",K - n)
        # print(min(number))
        # Min_number = min(number)
        # print(Min_number)
        # print("number",number)
        # Array.popleft()
    # number.append(K - n)
    # positive_numbers = [i for i in number if i >0 ]
    # print(min(positive_numbers))
    


# print("number:",number)
# positive_numbers = [i for i in number if i >0 ]
# print("positive_numbers:",positive_numbers)
# print(min(positive_numbers))




