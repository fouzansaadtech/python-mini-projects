#Task 10:Simple Calculator

n1=int(input("NO1:"))
n2=int(input("NO2:"))
operator=input("Selected Oparater '+' '-' '*' '/'")
if(operator=="+"):
    print(f"NO 1:{n1}\nNO 2:{n2} \nOperator:{operator}\nResults:{n1+n2}")
elif(operator=="-"):
    print(f"NO 1:{n1}\nNO 2:{n2} \nOperator:{operator}\nResults:{n1-n2}")
elif(operator=="*"):
    print(f"NO 1:{n1}\nNO 2:{n2} \nOperator:{operator}\nResults:{n1*n2}")
elif(operator=="/"):
    print(f"NO 1:{n1}\nNO 2:{n2} \nOperator:{operator}\nResults:{n1/n2}")
else:
    print("You Selected Operator Is Not Exists")