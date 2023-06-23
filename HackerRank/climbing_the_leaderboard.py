n = int(input())

ranked = list(map(int, input().split()))
deleteDup = list(set(ranked))

deleteDup.sort(reverse=True)

k = int(input())
player = list(map(int, input().split()))

def check (deleteDup, player):
    ranks = []
    
    current_rank = 1
    previous_score = None
    previous_rank = 1
    
    
    for playerScore in player:

        if playerScore < deleteDup[-1]:
            current_rank = len(deleteDup) +1
        else:
            for i in range(len(deleteDup)):
        
                if playerScore >= deleteDup[i]:
                    current_rank = i+1
                    break
                else:
                    current_rank = i+1  
       
        # ranks.append(current_rank)
        print(current_rank)
        previous_score =playerScore
        previous_rank = current_rank

    

check(deleteDup, player)
    


