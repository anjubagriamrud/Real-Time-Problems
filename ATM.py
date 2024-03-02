import time
print("PLEASE INSERT YOUR CARD:")
time.sleep(5)

password=1234
pin=int(input("ENTER YOUR ATM PIN"))
balance=5000

if(pin==password):
 while True:
        print(""" OPERAT1IONS CAN POSSIBLE::
        press 1 for : BALANCE ENQUIRY
        press 2 for : WITHDRAWL AMOUNT
        press 3 for : DEPOSIT BALANCE
        press 4 for : EXIT
          """)
        try:
            choice = int(input("enter your choice for operation:"))
        except:
            print("please enter valid choice.")
        if(choice==1):
           print(f"YOUR CURRENT BALANCE IS: {balance}")
        if(choice==2):
            withdrawl_amount=int(input("ENTER THE WITHDRAWLING AMOUNT: "))
            balance=balance-withdrawl_amount
            print(f"{withdrawl_amount} is debited from amount")
            print(f"NOW YOUR UPDATED BALANCE IS:{balance}")
        if(choice==3):
            deposit_amount=int(input("ENTER THE DEPOSTING AMOUNT: "))
            balance=balance+deposit_amount
            print(f"{deposit_amount} is added to your amount")
            print(f"NOW YOUR UPDATED BALANCE IS: {balance}")
        if(choice==4):
          print("THANKS PLEASE COME AGAIN.")
          break
else:
        print("wrong pin. please try again...")


