import random
c=random.randint(0,100)
u=int(input("Enter number between 0 to 100 : "))
print("Computer number is:", c )
if u>100:
    raise ValueError("Please enter the number between 0 to 100")
elif u>c:
    print("User number is greater that computer number")
elif u<c:
    print("User number is lesser than computer number")
elif u==c:
    print("User number is equal to computer number")





