import random

l=["rock", "paper", "scissor"]
while True:
    c_count=0
    u_count=0
    uc = int(input("""Game Start
1. Yes
2. No | Exit :
"""))
    if uc==1:
        for a in range(1,6):
            u = int(input("""
1. Rock
2. Paper
3. Scissor
"""))
            if uc==1:
                ui="rock"
            elif uc==2:
                ui="paper"
            elif u==3:
                ui="scissor"
            c=random.choice(l)
            print(c)
            if ui=="rock" and c=="paper":
                c_count=c_count+1
                print("You loose")
            elif ui=="paper"  and c=="scissor":
                c_count=c_count+1
                print("You loose")
            elif ui=="scissor" and c=="rock":
                c_count=c_count+1
                print("You loose")
            elif ui==c:
                c_count=c_count+1
                u_count=u_count+1
                print("Draw")
            else:
                u_count=u_count+1
                print("You win")

        print("")
        print("Computer count is :", c_count)
        print("User count is :", u_count)
        print("")

        if c_count>u_count:
            print("You loose")
        elif c_count<u_count:
            print("You win")
        elif c_count==u_count:
            print("Draw")
        print("")

    elif uc==2:
        print("Thank you for playing")
        break