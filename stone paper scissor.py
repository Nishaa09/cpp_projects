from random import choice
bag = ("stone", "paper", "scissor")
aura_count = 0
name_count = 0


def score(name, nscore, Ascore):
    print("-------------------")
    print("|     Scores      |")
    print("--------------------")
    print("|",name,"|   Aura  |")
    print("-------------------")
    print("|", nscore,"   |   ",  Ascore, "    |")
    print("--------------------")


name = input("Welcome to the Game\nSTONE PAPER SCISSOR\nplease insert your name\n")
print("okay!!", name, "lets begin the game,you are playing against Aura")
for i in range(5):

    choose=""
    while choose not in bag:
        choose = input("choose one from (stone,paper,scissor):\n")
    aura = choice(bag)
    print( name,"chose",choose )
    print("Aura chose",aura)

    if aura == choose:
        score(name, name_count, aura_count)
    elif aura == "stone":
        if choose == "paper":
            name_count += 1
            score(name, name_count, aura_count)
        elif choose == "scissor":
            aura_count += 1
            score(name, name_count, aura_count)

    elif aura == "paper":
        if choose == "scissor":
            name_count += 1
            score(name, name_count, aura_count)

        elif choose == "stone":
            aura_count += 1
            score(name, name_count, aura_count)

    elif aura == "scissor":
        if choose == "stone":
            name_count += 1
            score(name, name_count, aura_count)

        elif choose == "paper":
            aura_count += 1
            score(name, name_count, aura_count)
            

if name_count > aura_count:
    print("WOWW!!",name,"won the game")
elif aura_count > name_count:
    print("WOWW!! Aura won the game")
else:
    print("ohh ,ITS A DRAWWW")
