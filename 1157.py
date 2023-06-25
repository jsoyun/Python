import sys
sys.stdin = open('1157.txt','r')
n = input()
# n = list(map(int, input().split()))

def find_common_alphabet(text):
    #가장 중복 많은 애 찾기
    max_count = 0
    most_common_alphabet = None
    alphabet_count = {}
  
    #알파벳 빈도계산
    for char in text:
        char = char.lower()
        
        if char in alphabet_count:
            alphabet_count[char] += 1
        else:
            alphabet_count[char] = 1

        if alphabet_count[char] > max_count:
            max_count = alphabet_count[char]

            most_common_alphabet = char

        elif alphabet_count[char] == max_count:
            most_common_alphabet = "?"


    print(most_common_alphabet)

    

find_common_alphabet(n)