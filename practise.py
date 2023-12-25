for i in range(6):
    for k in range(i):
        print(" ", end=" ")
    for j in range(6-i):
        print("*", end=" ")
    for l in range(6-i-1):
       print("*", end=" ")
    print()