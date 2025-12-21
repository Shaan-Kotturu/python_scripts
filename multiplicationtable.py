#Multiplication table
table = int(input("Which multiplication table would you like to learn today?: "))
for x in range(1,11):
    y=x*table
    print(f"{table} x {x} = {y}")