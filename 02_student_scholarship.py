#Task 5 Student Scholarship System

n1=input("Student Name:")
n2=int(input("Marks 0 - 100:"))
if(n2>=0 and n2<=100):
    if(n2>=80):
     n3=int(input("Attendance Percentage:"))
     if(n3>=75):
         print("Scholarship Approved")
     else:
          print("Attendance Too Low")
    else:
       print("Marks Not Enough")
else:
   print("invalid")