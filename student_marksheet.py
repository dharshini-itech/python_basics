name=input("Enter student name:")
m1=int(input("Maths mark:"))
m2=int(input("Physics mark:"))
m3=int(input("Chemistry mark:"))

total=m1+m2+m3
average=total/3

if(m1>=35 and m2>=35 and m3>=35):
    print('result= pass')
    print('total=',total)
    print('average=',average)
    if (average>=90):
        print('GRADE A')
    elif(90>average>=80):
        print("GRADE B")
    elif(80>average>=70):
        print("GRADE C")
    else:
        print("GRADE D")
    print('ALL THE BEST FOR YOUR FUTURE')
else:
    print('result=fail')
    if m1<35:
        print("should write complemantary exam for maths")
    elif m2<35:
        print("should write complemantary exam for physics")
    elif m3<35:
        print("should write complemantary exam for chemistry")
    print('ALL THE BEST FOR YOUR FUTURE')
