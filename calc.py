import operator ; num1 = float(input("enter num1: ")) ; num2 = float(input("enter num2: ")) ; opt = input("enter operator: ") ; operator = {'+': operator.add,'-': operator.sub,'*': operator.mul,'//':operator.truediv} ; num3 = operator[opt](num1,num2) ; print("result is: " , num3)