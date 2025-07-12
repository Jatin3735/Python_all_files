import random

secret_number = random.randint(1,100)
print("Welcome To Our Game")
print("I have Select a number between 1 to 100")
print("Can  you guess it???")

attempt = 0

while True:
    try:
        choose = int(input("Enter your number: "))
        attempt+= 1
        if secret_number>choose:
            print("Number is small. Try again")
    
        elif secret_number < choose :
            print("Number is high. Try again")
    
        else:
            print(f"You Find This number in {attempt} attempts.")
    


    except ValueError:
      print('Invalid Choice. Please try again.')


    