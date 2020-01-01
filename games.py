import random
number = random.randint(1,1000)
attempts = 0
low = 1
high = 1000

while True:
    print("Guess The number between 1 to 1000: ")
    input_number = (low + high)//2
    attempts+=1
    if input_number == number:
        print("Yes, Your Guess is correct")
        break
    elif input_number > number:
        print("Incorrect! Try to guess a smaller number")
        high = input_number - 1
    else:
        print("Incorrect! Try to guess a large number")
        low = input_number + 1
print("You tried", attempts, "Times to find the correct number.", number)