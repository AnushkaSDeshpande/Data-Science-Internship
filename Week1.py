# Week 1: Introduction to Python Programming
# Create a basic data processing script

year= int(input("Enter a year: "))
if(year % 400 == 0):
    print(year, "is a leap year.")
elif(year % 100 == 0):
    print(year, "is not a leap year.")  
elif(year % 4 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

"""
Output:
Enter a year: 2000
2000 is a leap year.

Enter a year: 2005
2005 is not a leap year.
"""