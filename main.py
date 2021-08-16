import getpass
#     ans = getpass.getpass('Enter The Number :')




# chance = 0
# ans = input("Enter The Number :")
# for a in number:
#     if chance != 5:
#         ans=input("Guess The Number")
#         if ans > number:
#             print("Enter Some Less Number")
#             chance+1
#         elif ans < number:
#             print("Enter Some Big Number")
#             chance+1
#         else:
#             print("You Guess Right")
#             chance==5
#     else :
#         print("You are Out of Your Chance")


an = int(getpass.getpass('Enter The Number :'))
attempt = 0
while True:
    attempt += 1
    guess = int(input("Guess The Number : \n"))
    if guess < an:
        print("Your Guessed Number is Low")
    
    elif guess > an:
        print("Your Guessed Number is High")

    else:
        print(f"You Guessed The Number in {attempt} attempts")
        break
print("!!!Thanks For Playing!!!")
print(f"Guessed Number is {an}")