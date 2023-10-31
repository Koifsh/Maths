class main:
    def __init__(self):
        self.variables = {}
        self.equation = ":" + "2x**23 + 2y**2" + ";"
        for index,item in enumerate(self.equation):
            if item.isalpha():
                self.variables[item] = self.addvariables(index)
        print(self.variables)
    
    def addvariables(self,index):
        coefficient = ""
        indicy = ""
        if self.equation[index-1] == ":":
            coefficient = "1"
        else:
            for i in range(1,index):
                char = self.equation[index-i]
                if char.isdigit():
                    coefficient = char + coefficient 
                else:
                    break
                
        if not (self.equation[index+1] == "*" and self.equation[index+2] == "*"):
            indicy = "1"
            
        elif self.equation[index+1] == "*" and self.equation[index+2] == "*":
            for i in self.equation[index+3:]:
                print(i)
                if i.isdigit():
                    indicy = indicy + i
                else:
                    break
        return {"coeff": int(coefficient),"power": int(indicy)}
    
        
instance = main()