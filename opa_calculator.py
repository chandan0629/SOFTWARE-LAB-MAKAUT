S = int(input("Enter no. of Screens: "))
r = int(input("Enter no. of reports: "))
C = int(input("Enter no. of Components: "))

print("Enter 1 for Simple, 2 for Medium, and 3 for High:")
X = int(input())

if X == 1:
   op = S * 1 + r * 2 + C * 10
elif X == 2:
    op = S * 2 + r * 5 + C * 10
elif X == 3:
        op = S * 3 + r * 8 + C * 10

reuse = int(input("Enter reusability: "))
nop = op * (100 - reuse) / 100

print("Object point:", op)
print("New Object point:", nop)