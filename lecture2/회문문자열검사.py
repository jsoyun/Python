import sys
sys.stdin = open('input.txt','rt')
n = int(input())


for i in range(n):
    s = input()

    s =s.upper()
    # print("len(s)",len(s))


    for i in range(len(s)//2):
        # while i != len(s)-1-i:
        if s[i] != s[len(s)-1-i]:
            # continue 
            print("No")  
            break
    else:
        print("Yes")



