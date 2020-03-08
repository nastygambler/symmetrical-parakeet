import math
n =  20#int(input("enter a number"))
pt =[]
if n <=1: print("no pythogeran triplets found!!")
else:   
    for i in range(1,n**2+1):
        cint = int(math.sqrt(n**2 + i**2))
        c = (math.sqrt(n**2 + i**2))
        if c-cint == 0.0 : pt.append((n,i,cint))   
print(pt)    