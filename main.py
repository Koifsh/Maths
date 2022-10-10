from sympy import * 
import matplotlib.pyplot as plt
import numpy as np
x, y = symbols("x y")
# expression = eval(str(input("Enter your expression: ")))
expression = list(str(input("Enter your expression: ")))
evaluated = []
for i in expression:
    if i == "x":
        try:
            a = eval(evaluated[-1])
            evaluated.append("*")
        except:
            pass
        
    elif i == "^":
        evaluated.append("*")
        evaluated.append("*")
        continue
    
    evaluated.append(i)
exp = expand(eval("".join(evaluated)))
dif = diff(exp,x)
pprint(dif)
xvalues = solve(dif)
print(f"x = {xvalues}")
for i in xvalues:
    print(f"for {i}")
    print(f"f({i-0.1}) = {dif.subs(x,i-0.1)}")
    print(f"f({i+0.1}) = {dif.subs(x,i+0.1)}")
    ycoord = exp.subs(x,i)
    print(f"\ny = {ycoord}")
    print(f"P = ({i},{ycoord})\n")



# upperbound = float(input("Enter upper bound "))
# lowerbound = float(input("Enter lower bound "))
# upperline = str(input("Enter equation of the upper line "))
# lowerline = str(input("Enter equation of the lower line "))
# area = quad((lambda x: eval(upperline) - eval(lowerline)),lowerbound,upperbound)[0]
# print(area)

# # ∫ upper 2, lower -2 of (y=x^2 + 2)
# area = quad((lambda x: 6 - ( x**2 +2)),-2,2)
# print(area)

# # ∫ upper 6, lower 2 of (y=x^3)
# area = quad((lambda x: x**3),2,6)
# print(area)

# area = quad((lambda x: (6 * x - x**2) - (2 * x)),4,0)
# print(area)