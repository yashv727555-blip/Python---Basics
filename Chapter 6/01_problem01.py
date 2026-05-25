a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
c=int(input("Enter number 3: "))
d=int(input("Enter number 4: "))

if(a>b and  a>c and  a>d):
    print("Num 1 is greatest")

elif(b>a and b>c and b>d):
    print("Num 2 is greatest")

elif(c>b and c>a and c>d):
    print("C is greatest")
else:
    print("d IS greatest")