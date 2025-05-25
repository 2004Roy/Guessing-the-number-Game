import random

computer=random.randint(1,100)


c=0
while(computer>0):
    player=int(input("Enter your number between 1 and 100 : "))
    c+=1
    if(player>computer):
        print("Lower number please!!!")
        
    elif(player<computer):
        print("Higher number please!!!")
        
    else:
        print("You Win!!!")
        break

print("Your points : ",c)

