import random
option = ['rock','paper','scissors']
draw = 0
win = 0
lost = 0
for i in range(5):
    pos = random.randint(0, 2)
    cochoice = option[pos]

    mychoic = input("What is your choice between: rock , paper , scissors? ")
    if mychoic==cochoice:
        print("You choose:", mychoic)
        print("Computer choose:", cochoice)
        print("Result: It's drawn")
        draw += 1
    elif mychoic=="rock" and cochoice=="paper":
        print("You choose:", mychoic)
        print("Computer choose:", cochoice)
        print("Result: Computer Won")
        lost += 1
    elif mychoic == "paper" and cochoice == "scissors":
        print("You choose:", mychoic)
        print("Computer choose:", cochoice)
        print("Result: Computer Won")
        lost += 1
    else:
        print("You choose:", mychoic)
        print("Computer choose:", cochoice)
        print("Result: You Won")
        win +=1
print("Draw: ",draw ,"Win: ",win ,"Lost: ",lost)

if win==draw==lost:
    print("The final result is Draw")
elif(win<lost):
    print("You looser")
else:
    print("Winner! Winner!! Chicken Dinner!!!")

