import random
print("%%%%% STONE PAPER SCISSOR GAME ME APKA SWAAGAT H UMEED H APKO MZA AAYEGA %%%%%")
stone=0
paper=1
scissor=2
i=0
for i in range(5):
   computer_input = random.randrange(0,2)
   user_input=int(input("instructions: enter the number 0,1,or 2 :"))
   if(user_input>2 and user_input<0):
          print("please enter according to instructions: ")
   elif(user_input==computer_input):
          print("TIE!!! PLAY AGAIN...")
   elif(user_input==0 and computer_input==1):
          print("SORRY ! You lost!!!! ")
          print("The winner is ",computer_input,"means paper.")
   elif(user_input==1 and computer_input==0):
          print("Congrats! You win !!!!")
   elif(user_input==1 and computer_input==2):
          print("SORRY !! You lost!!!!")
          print("The winner is ", computer_input,"means scissor.")
   elif(user_input==2 and computer_input==1):
          print("Congrats!! You win !!!!")
   elif(user_input==0 and computer_input==2):
          print("Congrats!!! You win !!!!")
   elif (user_input == 2 and computer_input == 0):
          print("SORRY !!! You lost!!!!")
          print("The winner is ", computer_input,"means stone.")
   else:
          print("invalid input")
          print("The winner is ", computer_input ,"means computer")

