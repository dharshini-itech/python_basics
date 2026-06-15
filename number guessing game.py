guess=0
secret=78
print("HEYY!!,WELCOME")

while True:
    guess=int(input("enter a 2 digit number"))
    if guess==secret:
        print("Yeah,your correct")
        break
    elif(guess>secret):
        print("nope,your answer is too high")
    elif(guess<secret):
        print("nope,your answer is too low")
    a=input("DO YOU WANT TO CONTINUE THE GAME??(yes or no)")
    if a=="yes":
        continue
    else:
        print("THANKYOU!!,HAVE A NICE DAY")
        break

