# Task 5:Employee Bonus Calculator

salary=int(input("Salary:"))
if(salary>50000):
    print(f"Salary: {salary} \nBonus: {int(salary/100*10)}")
elif(salary>3000):
    print(f"Salary: {salary} \nBonus: {int(salary/100*5)}")
else:
    print(f"Salary: {salary} \nBonus: {int(salary/100*2)}")