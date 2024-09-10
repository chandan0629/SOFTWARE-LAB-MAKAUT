a=int(input("enter the number of inputs: "))
b=int(input("enter the number of outputs: "))
c=int(input("enter the number of enquiries: "))
d=int(input("enter the number of files: "))
e=int(input("enter the number of iterfaces: "))

wi=4
wo=5
we=4
wf=10
wn=7

ufp=(a*wi)+(b*wo)+(c*we)+(d*wf)+(e*wn)
f1=0
f2=3
f3=4

sumf=(4*f1)+(4*f2)+(6*f3)
caf=0.65+(0.01*sumf)
fp=ufp*caf
print(f"Computed value of Unadjusted Function Points (UFP): {ufp}")
print(f"Computed value of Function Points (FP): {fp}")
print(f"Computed value of Complexity Adjustment Factor (CAF): {caf}")

