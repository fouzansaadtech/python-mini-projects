# Task 9:Online Shopping Discount

Amount=int(input("Amount:"))
if(Amount>5000):
    print(f"Amount: {Amount} \nDiscount: {int(Amount/100*20)}\nFinal Amount: {int(Amount-Amount/100*20)}")
elif(Amount>=2000):
    print(f"Amount: {Amount} \nDiscount: {int(Amount/100*10)}\nFinal Amount: {int(Amount-Amount/100*10)}")
else:
    print(f"Amount: {Amount} \nDiscount: No  \nFinal Amount: {Amount}")