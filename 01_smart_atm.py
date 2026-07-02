# Smart ATM Login System

pin = int(input("Enter ATM PIN: "))

if pin == 1234:
    amount = int(input("Enter Withdrawal Amount: "))

    if 100 <= amount <= 5000:
        print("Transaction Successful")
    else:
        print("Invalid Withdrawal Amount")
else:
    print("Invalid PIN")