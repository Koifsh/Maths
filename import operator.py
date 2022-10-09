import operator
from sympy import symbols, Eq, solve


def integration():
    y = True
    cont = True
    aOpAdd = False
    bOpAdd = False
    cOpAdd = False

    solveList = []
    finalValues = []
    d ={}
    counter = 0

    while cont == True:
        while y == True:
            counter += 1
            x = symbols("x")
            a = int(input("Enter a: "))
            aOp = str(input("Enter +/-: "))
            if aOp == "+":
                aOpAdd = True
            else:
                aOpAdd = False
            powerA = int(input("Enter power: "))
            b = int(input("Enter b: "))
            bOp = str(input("Enter +/-: "))
            if bOp == "+":
                bOpAdd = True
            else:
                bOpAdd = False
            powerB = int(input("Enter power: "))
            c = int(input("Enter c: "))
            cOp = str(input("Enter +/-: "))
            if cOp == "+":
                cOpAdd = True
            else:
                cOpAdd = False
            if aOpAdd == False and bOpAdd == True and cOpAdd == True:
                inputY = str(input(f"Is the equation: -{a}x^{powerA}+{b}x^{powerB}+{c}x "))
                if inputY != "y":
                    y = False
                    continue
                else:
                    y = True
                    inPutY2 = str(input(f"Is the differentiated equation: {(a*-1)*powerA}x^{powerA-1}+{b*powerB}x^{powerB-1}+{c} "))
                    if inPutY2 != "y":
                        y = False
                        continue
                    else:
                        y = True
                        expr = -(((a*-1)*powerA))*x**((powerA-1))+((b*powerB))*x**((powerB-1))+(c)
                        d["solve{0}".format(counter)] = solve(expr)
                        print(d)
                        for i in range(0,(len(d["solve{0}".format(counter)]))):
                            num = d["solve{0}".format(counter)]
                            finalValues.append(num[i])
                            value = num[i] + 0.1
                            expr2 = expr.subs(x, round(value, 3))
                            print(f"{num[i]} + 0.1 means m = {expr2} when x = {round(value, 2)}")
                            finalValues.append(expr2)
                        for i in range(0,(len(d["solve{0}".format(counter)]))):
                            num = d["solve{0}".format(counter)]
                            finalValues.append(num[i])
                            value = num[i] - 0.1
                            expr2 = expr.subs(x, round(value, 3))
                            print(f"{num[i]} - 0.1 means m = {expr2} when x = {round(value, 2)}")
                            finalValues.append(expr2)
                        if len(finalValues) == 8:
                            print(f"{finalValues[0]} = [{finalValues[1]},{finalValues[5]}]")
                            print(f"{finalValues[2]} = [{finalValues[2]},{finalValues[7]}]")
                            if finalValues[1] > 0:
                                print(f"""x = {finalValues[0]} is max point
    x = {finalValues[2]} is min point""")
                            else:
                                print(f"""x = {finalValues[2]} is max point
    x = {finalValues[0]} is min point""")
                        elif len(finalValues) == 12:
                            print()
                        contInput = str(input("Continue?"))
                        if contInput == "y":
                            cont = True
                            continue
                        else:
                            cont = False
                            continue
                        continue
            elif aOpAdd == False and bOpAdd == False and cOpAdd == True:
                inputY = str(input(f"Is the equation: -{a}x^{powerA}-{b}x^{powerB}+{c}x "))
                if inputY != "y":
                    y = False
                    continue
                else:
                    y = True
                    inPutY2 = str(input(f"Is the differentiated equation: {(a*-1)*powerA}x^{powerA-1}-{(b*-1)*powerB}x^{powerB-1}+{c} "))
                    if inPutY2 != "y":
                        y = False
                        continue
                    else:
                        y = True
                        expr = -((a*-1)*powerA)*x**((powerA-1))+(((b*-1)*powerB))*x**((powerB-1))+(c)
                        d["solve{0}".format(counter)] = solve(expr)
                        print(d)
                        for i in range(0,(len(d["solve{0}".format(counter)]))):
                            num = d["solve{0}".format(counter)]
                            finalValues.append(num[i])
                            value = num[i] + 0.1
                            expr2 = expr.subs(x, round(value, 3))
                            print(f"{num[i]} + 0.1 means m = {expr2} when x = {round(value, 2)}")
                            finalValues.append(expr2)
                        for i in range(0,(len(d["solve{0}".format(counter)]))):
                            num = d["solve{0}".format(counter)]
                            finalValues.append(num[i])
                            value = num[i] - 0.1
                            expr2 = expr.subs(x, round(value, 3))
                            print(f"{num[i]} - 0.1 means m = {expr2} when x = {round(value, 2)}")
                            finalValues.append(expr2)
                        if len(finalValues) == 8:
                            print(f"{finalValues[0]} = [{finalValues[1]},{finalValues[5]}]")
                            print(f"{finalValues[2]} = [{finalValues[2]},{finalValues[7]}]")
                            if finalValues[1] > 0:
                                print(f"""x = {finalValues[0]} is max point
    x = {finalValues[2]} is min point""")
                            else:
                                print(f"""x = {finalValues[2]} is max point
    x = {finalValues[0]} is min point""")
                        elif len(finalValues) == 12:
                            print()
                        contInput = str(input("Continue?"))
                        if contInput == "y":
                            cont = True
                            continue
                        else:
                            cont = False
                            continue
                        continue
            elif aOpAdd == False and bOpAdd == False and cOpAdd == False:
                inputY = str(input(f"Is the equation: -{a}x^{powerA}-{b}x^{powerB}-{c}x "))
                if inputY != "y":
                    y = False
                    continue
                else:
                    y = True
                    inPutY2 = str(input(f"Is the differentiated equation: {(a*-1)*powerA}x^{powerA-1}+{(b*-1)*powerB}x^{powerB-1}+{(c*1)} "))
                    if inPutY2 != "y":
                        y = False
                        continue
                    else:
                        y = True
                        expr = -(((a*-1)*powerA))*x**((powerA-1))-((b*-1*powerB))*x**((powerB-1))-(c*1)
                        d["solve{0}".format(counter)] = solve(expr)
                        print(d)
                        for i in range(0,(len(d["solve{0}".format(counter)]))):
                            num = d["solve{0}".format(counter)]
                            finalValues.append(num[i])
                            value = num[i] + 0.1
                            expr2 = expr.subs(x, round(value, 3))
                            print(f"{num[i]} + 0.1 means m = {expr2} when x = {round(value, 2)}")
                            finalValues.append(expr2)
                        for i in range(0,(len(d["solve{0}".format(counter)]))):
                            num = d["solve{0}".format(counter)]
                            finalValues.append(num[i])
                            value = num[i] - 0.1
                            expr2 = expr.subs(x, round(value, 3))
                            print(f"{num[i]} - 0.1 means m = {expr2} when x = {round(value, 2)}")
                            finalValues.append(expr2)
                        if len(finalValues) == 8:
                            print(f"{finalValues[0]} = [{finalValues[1]},{finalValues[5]}]")
                            print(f"{finalValues[2]} = [{finalValues[2]},{finalValues[7]}]")
                            if finalValues[1] > 0:
                                print(f"""x = {finalValues[0]} is max point
    x = {finalValues[2]} is min point""")
                            else:
                                print(f"""x = {finalValues[2]} is max point
    x = {finalValues[0]} is min point""")
                        elif len(finalValues) == 12:
                            print()
                        contInput = str(input("Continue?"))
                        if contInput == "y":
                            cont = True
                            continue
                        else:
                            cont = False
                            continue
                        continue
            elif aOpAdd == True and bOpAdd == True and cOpAdd == True:
                inputY = str(input(f"Is the equation: {a}x^{powerA}+{b}x^{powerB}+{c}x "))
                if inputY != "y":
                    y = False
                    continue
                else:
                    y = True
                    inPutY2 = str(input(f"Is the differentiated equation: {a*powerA}x^{powerA-1}+{b*powerB}x^{powerB-1}+{c} "))
                    if inPutY2 != "y":
                        y = False
                        continue
                    else:
                        y = True
                        expr = ((a*powerA))*x**((powerA-1))+((b*powerB))*x**((powerB-1))+(c)
                        d["solve{0}".format(counter)] = solve(expr)
                        print(d)
                        for i in range(0,(len(d["solve{0}".format(counter)]))):
                            num = d["solve{0}".format(counter)]
                            finalValues.append(num[i])
                            value = num[i] + 0.1
                            expr2 = expr.subs(x, round(value, 3))
                            print(f"{num[i]} + 0.1 means m = {expr2} when x = {round(value, 2)}")
                            finalValues.append(expr2)
                        for i in range(0,(len(d["solve{0}".format(counter)]))):
                            num = d["solve{0}".format(counter)]
                            finalValues.append(num[i])
                            value = num[i] - 0.1
                            expr2 = expr.subs(x, round(value, 3))
                            print(f"{num[i]} - 0.1 means m = {expr2} when x = {round(value, 2)}")
                            finalValues.append(expr2)
                        if len(finalValues) == 8:
                            print(f"{finalValues[0]} = [{finalValues[1]},{finalValues[5]}]")
                            print(f"{finalValues[2]} = [{finalValues[2]},{finalValues[7]}]")
                            if finalValues[1] > 0:
                                print(f"""x = {finalValues[0]} is max point
    x = {finalValues[2]} is min point""")
                            else:
                                print(f"""x = {finalValues[2]} is max point
    x = {finalValues[0]} is min point""")
                        elif len(finalValues) == 12:
                            print()
                        contInput = str(input("Continue?"))
                        if contInput == "y":
                            cont = True
                            continue
                        else:
                            cont = False
                            continue
                        continue
            elif aOpAdd == True and bOpAdd == True and cOpAdd == False:
                inputY = str(input(f"Is the equation: {a}x^{powerA}+{b}x^{powerB}-{c}x "))
                if inputY != "y":
                    y = False
                    continue
                else:
                    y = True
                    inPutY2 = str(input(f"Is the differentiated equation: {(a)*powerA}x^{powerA-1}+{b*powerB}x^{powerB-1}-{c*-1} "))
                    if inPutY2 != "y":
                        y = False
                        continue
                    else:
                        y = True
                        expr = ((a*powerA))*x**((powerA-1))+((b*powerB))*x**((powerB-1))-(c*-1)
                        d["solve{0}".format(counter)] = solve(expr)
                        print(d)
                        for i in range(0,(len(d["solve{0}".format(counter)]))):
                            num = d["solve{0}".format(counter)]
                            finalValues.append(num[i])
                            value = num[i] + 0.1
                            expr2 = expr.subs(x, round(value, 3))
                            print(f"{num[i]} + 0.1 means m = {expr2} when x = {round(value, 2)}")
                            finalValues.append(expr2)
                        for i in range(0,(len(d["solve{0}".format(counter)]))):
                            num = d["solve{0}".format(counter)]
                            finalValues.append(num[i])
                            value = num[i] - 0.1
                            expr2 = expr.subs(x, round(value, 3))
                            print(f"{num[i]} - 0.1 means m = {expr2} when x = {round(value, 2)}")
                            finalValues.append(expr2)
                        if len(finalValues) == 8:
                            print(f"{finalValues[0]} = [{finalValues[1]},{finalValues[5]}]")
                            print(f"{finalValues[2]} = [{finalValues[2]},{finalValues[7]}]")
                            if finalValues[1] > 0:
                                print(f"""x = {finalValues[0]} is max point
    x = {finalValues[2]} is min point""")
                            else:
                                print(f"""x = {finalValues[2]} is max point
    x = {finalValues[0]} is min point""")
                        elif len(finalValues) == 12:
                            print()
                        contInput = str(input("Continue?"))
                        if contInput == "y":
                            cont = True
                            continue
                        else:
                            cont = False
                            continue
                        continue
            elif aOpAdd == True and bOpAdd == False and cOpAdd == False:
                inputY = str(input(f"Is the equation: {a}x^{powerA}-{b}x^{powerB}-{c}x "))
                if inputY != "y":
                    y = False
                    continue
                else:
                    y = True
                    inPutY2 = str(input(f"Is the differentiated equation: {(a)*powerA}x^{powerA-1}-{(b*-1)*powerB}x^{powerB-1}-{c*-1} "))
                    if inPutY2 != "y":
                        y = False
                        continue
                    else:
                        y = True
                        expr = ((a*powerA))*x**((powerA-1))-(((b*-1)*powerB))*x**((powerB-1))-(c*-1)
                        d["solve{0}".format(counter)] = solve(expr)
                        print(d)
                        for i in range(0,(len(d["solve{0}".format(counter)]))):
                            num = d["solve{0}".format(counter)]
                            finalValues.append(num[i])
                            value = num[i] + 0.1
                            expr2 = expr.subs(x, round(value, 3))
                            print(f"{num[i]} + 0.1 means m = {expr2} when x = {round(value, 2)}")
                            finalValues.append(expr2)
                        for i in range(0,(len(d["solve{0}".format(counter)]))):
                            num = d["solve{0}".format(counter)]
                            finalValues.append(num[i])
                            value = num[i] - 0.1
                            expr2 = expr.subs(x, round(value, 3))
                            print(f"{num[i]} - 0.1 means m = {expr2} when x = {round(value, 2)}")
                            finalValues.append(expr2)
                        if len(finalValues) == 8:
                            print(f"{finalValues[0]} = [{finalValues[1]},{finalValues[5]}]")
                            print(f"{finalValues[2]} = [{finalValues[2]},{finalValues[7]}]")
                            if finalValues[1] > 0:
                                print(f"""x = {finalValues[0]} is max point
    x = {finalValues[2]} is min point""")
                            else:
                                print(f"""x = {finalValues[2]} is max point
    x = {finalValues[0]} is min point""")
                        elif len(finalValues) == 12:
                            print()
                        contInput = str(input("Continue?"))
                        if contInput == "y":
                            cont = True
                            continue
                        else:
                            cont = False
                            continue
                        continue
            elif aOpAdd == True and bOpAdd == False and cOpAdd == True:
                inputY = str(input(f"Is the equation: +{a}x^{powerA}-{b}x^{powerB}+{c}x "))
                if inputY != "y":
                    y = False
                    continue
                else:
                    y = True
                    inPutY2 = str(input(f"Is the differentiated equation: {(a)*powerA}x^{powerA-1}-{(b*-1)*powerB}x^{powerB-1}+{c} "))
                    if inPutY2 != "y":
                        y = False
                        continue
                    else:
                        y = True
                        expr = ((a*powerA))*x**((powerA-1))-(((b*-1)*powerB))*x**((powerB-1))+(c)
                        d["solve{0}".format(counter)] = solve(expr)
                        print(d)
                        for i in range(0,(len(d["solve{0}".format(counter)]))):
                            num = d["solve{0}".format(counter)]
                            finalValues.append(num[i])
                            value = num[i] + 0.1
                            expr2 = expr.subs(x, round(value, 3))
                            print(f"{num[i]} + 0.1 means m = {expr2} when x = {round(value, 2)}")
                            finalValues.append(expr2)
                        for i in range(0,(len(d["solve{0}".format(counter)]))):
                            num = d["solve{0}".format(counter)]
                            finalValues.append(num[i])
                            value = num[i] - 0.1
                            expr2 = expr.subs(x, round(value, 3))
                            print(f"{num[i]} - 0.1 means m = {expr2} when x = {round(value, 2)}")
                            finalValues.append(expr2)
                        if len(finalValues) == 8:
                            print(f"{finalValues[0]} = [{finalValues[1]},{finalValues[5]}]")
                            print(f"{finalValues[2]} = [{finalValues[2]},{finalValues[7]}]")
                            if finalValues[1] > 0:
                                print(f"""x = {finalValues[0]} is max point
    x = {finalValues[2]} is min point""")
                            else:
                                print(f"""x = {finalValues[2]} is max point
    x = {finalValues[0]} is min point""")
                        elif len(finalValues) == 12:
                            print()
                        contInput = str(input("Continue?"))
                        if contInput == "y":
                            cont = True
                            continue
                        else:
                            cont = False
                            continue
                        continue
            elif aOpAdd == False and bOpAdd == True and cOpAdd == False:
                inputY = str(input(f"Is the equation: -{a}x^{powerA}+{b}x^{powerB}-{c}x "))
                if inputY != "y":
                    y = False
                    continue
                else:
                    y = True
                    inPutY2 = str(input(f"Is the differentiated equation: {(a*-1)*powerA}x^{powerA-1}+{b*powerB}x^{powerB-1}-{c*-1} "))
                    if inPutY2 != "y":
                        y = False
                        continue
                    else:
                        y = True
                        expr = -(((a*-1)*powerA))*x**((powerA-1))+((b*powerB))*x**((powerB-1))-(c*-1)
                        d["solve{0}".format(counter)] = solve(expr)
                        print(d)
                        for i in range(0,(len(d["solve{0}".format(counter)]))):
                            num = d["solve{0}".format(counter)]
                            finalValues.append(num[i])
                            value = num[i] + 0.1
                            expr2 = expr.subs(x, round(value, 3))
                            print(f"{num[i]} + 0.1 means m = {expr2} when x = {round(value, 2)}")
                            finalValues.append(expr2)
                        for i in range(0,(len(d["solve{0}".format(counter)]))):
                            num = d["solve{0}".format(counter)]
                            finalValues.append(num[i])
                            value = num[i] - 0.1
                            expr2 = expr.subs(x, round(value, 3))
                            print(f"{num[i]} - 0.1 means m = {expr2} when x = {round(value, 2)}")
                            finalValues.append(expr2)
                        if len(finalValues) == 8:
                            print(f"{finalValues[0]} = [{finalValues[1]},{finalValues[5]}]")
                            print(f"{finalValues[2]} = [{finalValues[2]},{finalValues[7]}]")
                            if finalValues[1] > 0:
                                print(f"""x = {finalValues[0]} is max point
    x = {finalValues[2]} is min point""")
                            else:
                                print(f"""x = {finalValues[2]} is max point
    x = {finalValues[0]} is min point""")
                        elif len(finalValues) == 12:
                            print()
                        contInput = str(input("Continue?"))
                        if contInput == "y":
                            cont = True
                            continue
                        else:
                            cont = False
                            continue
                        continue
            else:
                print("Error: Identifying Operations")
            print("End of while y == True loop")
        print("End of cont == True loop")
                        
                        
integration()


