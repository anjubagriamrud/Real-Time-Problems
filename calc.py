print("$$$$ WELCOME TO MY CALCULATOR $$$$ ")

for i in range(0,2):
     num1=int(input("Enter number 1: "))
     num2=int(input("Enter number 2: "))
     op=int(input("Enter as according to instructions:1 for addition,2 for subtraction,"
             "3 for multiplication, 4 for division and 5 for modulus."))
     if op==1:
            print("The addition of {} and {} is {}".format(num1,num2,num1+num2))
     elif op==2:
            print("The subtraction of {} and {} is {}".format(num1, num2, num1 - num2))
     elif op==3:
            print("The multiplication of {} and {} is {}".format(num1, num2, num1 * num2))
     elif op==4:
            print("The division of {} and {} is {}".format(num1, num2, num1 / num2))
     elif op==5:
            print("The modulus of {} and {} is {}".format(num1, num2, num1 % num2))
     else:
            print("please enter valid input:  ")

print(" @@@@ THANKS FOR USING MY CALCULATOR @@@@ ")