# Task 2 Mobile Unlock System

Password=input("Password:")
if(Password=="python123"):
    battery=int(input("Battery Percentage"))
    if(battery>=20 and battery<=100):
       print("Mobile Unlocked")
    else:
       print("Battery Too Low")
else:
   print("Wrong Password")