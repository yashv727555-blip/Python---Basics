m1=int(input("Enter m1: "))
m2=int(input("Enter m2: "))
m3=int(input("Enter m3: "))

if (m1 >32 and m2>32 and m3>33):
    print("Student has passed in each individual sub")
    t=((m1 + m2+ m3)/300)*100
    if(t>39):
        print("Student has passed all over")

else:
    print("Not passed")


