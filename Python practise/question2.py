# Program to print Letter U

for i in range(0,4):
    for j in range(0,5):
        if j==0 or j==4 or i==3:
            print('* ',end="")
        else: 
            print("  ",end="")
    print("\n")