#While Loops
# i =0
# while(i<45):
#     print(i)
#     i = i+1
    #when to use for and While--

#Break and Continue------
# i = 0
# while(True):
#     if i+1<5:
#         i = i + 1
#         continue
#      print(i+1, end="")
#      if(i == 44):
#           break
#           i = i+1


#---------Quiz_________-
while(True):
    inp = int(input("Enter teh number\n"))
    if inp>100:
        print("Congrats you have entered a number greater than 100")
        break
    else:
        print("Try again please!\n")
        continue