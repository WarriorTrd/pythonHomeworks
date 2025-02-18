#Questions
#1   quiz -10/13
#2  continue skip process after it once, break will exit the loop
#3  in for loop number of iteration is known, in while loop it is unknown
#4  another loop inside the loop
#      for i in range(10):
#          for j in range(10):
#          print(i, j)



#problem 1
# list1 = [1, 1, 2]
# list2 = [2, 3, 4]#
# list3=[]
# for i in list1:
#     if i not in list2:
#         list3.append(i)

# for i in list2:
#     if i not in list1:
#         list3.append(i)

# print(list3)        



#problem 2
# num=int(input("enter your num: "))
# i=1
# while i<num:
#     print(i*i)
#     i+=1

#problem 3
# txt = input("Enter your text: ")
# changed = ""
# count = 0
# vowels = "aeiouAEIOU"

# for i in range(len(txt)):
#     changed += txt[i]
#     count += 1
    
    
#     if count == 3 and txt[i] not in vowels:
#         changed += "_"
#         count = 0 

# print(changed)

       
#problem 4
# from random import *

# randnum=randint(1,100)
# trial=1
# while trial<=10:
#     num=int(input("enter your guess: "))
#     trial+=1
#     if num==randnum:
#         print("congrats u fount it!")
#         break
#     else:
#         print("sorry wrong number :(")
           
# else:
#     print(f"sorry it was your last chance,number was {randnum}u lost the game :(")
#     choise=input("do u wonna play again  ,if so enter one of the following \n'yes',\n'YES',\n'y',\n'Y' ")
#     if choise in ['yes','YES','y','Y']:
#         trial=0
#         randnum=randint(1,100)
#     else:
#         print("ok goodbye")    


#problem 5
# password = input("Enter the password: ")
# if len(password)<8:
#     print("Password is too short")
# if password.lower() == password:
#     print("Password must contain an uppercase letter.")
# if len(password)>8 and password.lower() != password:
#     print("Password is strong.")    
            
#problem 6
# for i in range(2, 100): 
#     prime = True  
#     for j in range(2, int(i**0.5) + 1):  
#         if i % j == 0:  
#             prime = False
#             break  
    
#     if prime:  
#         print(i)


#bonus problem 
# from random import*


# count_comp=0
# count_player=0
# while count_comp<5 and count_player<5:
#     player=input("what do u choose rock,paper or Scissors: ").lower()
#     comp=choice(["rock","paper","Scissors"])
#     if player=="rock" and comp=="rock":
#          print("It's a tie!")
        
#     elif player=="rock" and comp=="paper":
#         count_comp+=1
#         print("Computer wins this round!")
#     elif player=="rock" and comp=="scissors": 
#         count_player+=1  
#         print("You win this round!") 
#     elif player=="scissors" and comp=="scissors": 
#          print("It's a tie!") 
#     elif player=="scissors" and comp=="rock": 
#         count_comp+=1
#         print("Computer wins this round!")
    
#     elif player=="scissors" and comp=="paper":
#         count_player+=1
#         print("You win this round!")
#     elif player=="paper" and comp=="paper":
#          print("It's a tie!")
#     elif player=="paper" and comp=="scissors":
#         count_comp+=1
#         print("Computer wins this round!")
#     else:
#         count_player+=1
#         print("You win this round!")


# if count_player == 5:
#     print("Congratulations! You won the game!")
# else:
#     print("Sorry, the computer won the game.")        



        








