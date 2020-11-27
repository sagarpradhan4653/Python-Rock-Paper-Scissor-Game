# Rock Papper Scissors

import random

def game(comp, you):
    if comp == you:
        return None

    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False



    
print("Comp: Rock(r) Papper(p) Scissor(s)? ")
rndm = random.randint(1,3)
if rndm == 1:
    comp = "r"
elif rndm == 2:
    comp = "p"
elif rndm == 3:
    comp = "s"

you = input("You: Rock(r) Papper(p) Scissor(s)? ")
a = game(comp, you)

print(f"Comp choose {comp} ")

if a == None:
    print("The game is tie")
elif a:
    print("You Win!!")
else:
    print("You Loose!!")
