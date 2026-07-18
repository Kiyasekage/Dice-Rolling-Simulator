import random
print("Welcome to rolling your dice!")
ans = 'Y'
while ans=='Y':
    print(f"Dice 1 : {random.randint(1,6)}\nDice 2 : {random.randint(1,6)}")
    ans = input("Do you want to continue(Y/N)").upper()
    if ans=='N':
        break
print("Thankyou for using our program!")
