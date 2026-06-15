number1=int(input("enter a number:"))
number2=int(input("enter another number:"))
symbol=input("give your operators:")

if(symbol=="+"):
    print("sum of the given numbers=",number1+number2)
elif(symbol=="-"):
    print("difference between the given 2 numbers=",number1-number2)
elif(symbol=="*"):
    print("product of the given 2 numbers=",number1*number2)
elif(symbol=="/"):
    print("division=",number1/number2)
else:
    print("check your operator")
