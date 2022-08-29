import time
import random

iterations = 500
wins = 0

for i in range(iterations):
    door = random.randint(1,3)
    choice = random.randint(1,3)
    
    if choice == 1:
        if door != 2:
            choice = 3
        else:
            choice = 2
    elif choice == 2:
        if door != 1:
            choice = 3
        else:
            choice = 1
    else:
        if door != 1:
            choice = 2
        else:
            choice = 1
            
    if choice == door:
        wins += 1
        
winRate = float(wins) / float(iterations)
print("Taux de réussite : " + str(winRate))

time.sleep(2)