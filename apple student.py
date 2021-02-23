# N students takes K apples distributes among each other evenly. The remaining (undivisible) part remains in the basket. How many apples will each single student get?
#How many apples will remain in the basket ? The program reads the number N and K. It should print the two answer for the questiom above.

stu=int(input('Enter the number of student:'))
app=int(input('Enter the number of apple:'))
div=(app/stu)
rem=(app%stu)
print("Each student gets",div)
print("Remaining apples in the basket",rem)
