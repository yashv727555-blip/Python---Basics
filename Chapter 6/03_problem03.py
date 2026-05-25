p1="Make a lot of money" # program to detect spam coment
p2= "Buy now"
p3="Subscribe now"
p4="Click this"

msg=input("Enter value of msg: ")

if (p1 in msg or p2 in msg or p3 in msg or p4 in msg):
    print("Bhaago bc")

else:
    ("proceed further")