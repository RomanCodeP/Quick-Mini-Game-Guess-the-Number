import random
r = random.randrange(100)
print(r)
print("Welcome to the Guess the number, ")
print("you have to input an interger from 1-100")
print("The program is going to give you hints")
attempts = 10
while True:
    print("-------------------")
    print("-------------------")
    print(f"you have {attempts} Left")
    try:
        x = int(input("Input a number from 1-100: "))
    except:
        print("You have to input an integer 1-100")
        break
        
    if x > r:
        print("Your number is bigger ⬇️")
        attempts = attempts - 1
        if attempts == 0:
            print("you ran out of attempts")
            break

    elif x < r:
        print("Your number is smaller ⬆️")
        attempts = attempts - 1
        if attempts == 0:
            print("you ran out of attempts")
            break
    elif x == r:
        print("Correct! The number is:", r)
        break
