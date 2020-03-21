"""
    Question :
        Create a basic bank cash dispenser
"""


def account(Name, Balance):
    accounta = {
        'Name': Name,
        'Balance': Balance
    }
    return accounta


def BalanceDisplay(balance):
    print(f"Your Balance is : {balance}")


def Withdraw(balance):
    withdraw = float(input("Enter value for withdraw \n"))
    if(withdraw > balance):
        print("You cant withdraw this value !!!")
    else:
        balance = balance - withdraw
        print(f"Your new balance = {balance}")


def Deposit(balance):
    depoist = float(input("Enter value for deposit \n"))
    balance += depoist
    print(f"Your new balance = {balance}")


Name = input("Account holder name : ")
Balance = float(input("Your Budget : "))
accounthold = account(Name, Balance)

print(accounthold)

print('\nSelect your Action\n')
x = int(input("1->Balance Display \n2->Withdraw \n3->Deposit \n4->Exit \n"))

choice = 0

while True:
    if(x == 1):
        BalanceDisplay(Balance)
    elif(x == 2):
        Withdraw(Balance)
    elif(x == 3):
        Deposit(Balance)
    else:
        break

    print('Select your Action\n')
    x = int(input("1->Balance Display \n2->Withdraw \n3->Deposit \n4->Exit \n"))
