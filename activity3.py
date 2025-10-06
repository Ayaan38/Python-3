number = int(input("Enter number to be checked"))
print("Number to be checked :", number)

if number%2==0 :
   print("This is an even number")

else :
    print("This is an odd number")

number = 28
if number>50 :
   print("Yes")
elif number<50 :
   print("No")
else :
   print("Invalid")

height=float(input("Enter your height in cm: "))
weight=float(input("Enter your weight in kg : "))
BMI = weight/ (height/100)**2
print("Your BMI is ",BMI)

if BMI <= 20 :
   print("You are underweight")
elif BMI <= 40 :
   print("You are healthy")
elif BMI <= 60 :
   print("You are overwight")
elif BMI <= 80:
   print("You are severly overweight")
elif BMI <= 100:
   print("You are obese")
else :
   print("You are severly obese")

num = float(input("Enter your age"))
if num >=0:
   if num >=18:
      print("Adult")
   else :
      print("Underage")
else :
   print("Wrong input")

num = int(input("Enter a number :"))

if num>50 :
   print("Number is greater than 50")
   if num%2 ==0 :
      print("it is even too")
   else :
      print("it is odd")
else :
   print("Number is less than 50")

import datetime
# using now to get current time
current_time = datetime.datetime.now()

print("Time now in Islamabad is :", "=")
print(current_time)

import calendar
print("/n", calendar.calendar(2024))