import textwrap
def menu(): 
   menu = """\n
   =============== MENU ===============
     [1]\tPut
     [2]\tWithdraw
     [3]\tBankStatement
     [4]\tNew User
     [5]\tNew Account
     [6]\tList Accounts
     [7]\tExit
   ===================================
   => """
   return input(textwrap.dedent(menu))

def Put(Balance, Value, BankStatement, /):
    if Value > 0:
        Balance += Value
        BankStatement += f"Deposit:\tR$ {Value:.2f}\n"
        print("\n=== Deposit made successfully! ===")
    else:
        print("\n@@@ Operation failed! The value entered is invalid. @@@")

    return Balance, BankStatement

def Withdraw(*, Balance, Value, BankStatement, Bound, NumberWithdraw, Bound_Withdraw):
    ExcededBalance = Value > Balance
    ExcededBound = Value > Bound
    ExcededWithdraw = NumberWithdraw >= Bound_Withdraw

    if ExcededBalance:
        print("\n@@@ Operation failed! You do not have enough Balance. @@@")

    elif ExcededBound:
        print("\n@@@ Operation failed! Withdrawal amount exceeds Bound. @@@")

    elif ExcededWithdraw:
        print("\n@@@ Operation failed! Maximum number of Withdraws exceeded. @@@")

    elif Value > 0:
        Balance -= Value
        BankStatement += f"Withdraw:\t\tR$ {Value:.2f}\n"
        NumberWithdraw += 1
        print("\n=== Withdraw successfully completed! ===")

    else:

        return Balance, BankStatement

def exibir_BankStatement(Balance, /, *, BankStatement):
    print("\n================ BankStatement ================")
    print("No movements were made." if not BankStatement else BankStatement)
    print(f"\nBalance:\t\tR$ {Balance:.2f}")
    print("==========================================")

def CreateUser(Users):
    cpf = input("Enter your CPF (number only): ")
    User = FilterUser(cpf, Users)

    if User:
        print("\n@@@ There is already a user with this CPF! @@@")
        return

    Name = input("Enter your full name: ")
    DateOfBirth = input("Enter your date of birth (dd-mm-yyyy): ")
    Address = input("Enter the address (street, number - neighborhood - city/state abbreviation): ")

    Users.append({"Name": Name, "DateOfBirth": DateOfBirth, "cpf": cpf, "Address": Address})

    print("=== User created successfully! ===")

def FilterUser(cpf, Users):
    UsersFiltered = [User for User in Users if User["cpf"] == cpf]
    return UsersFiltered[0] if UsersFiltered else None

def CreateAccount(Agency, AccountNumber, Users):
    cpf = input("Enter the user's CPF: ")
    User = FilterUser(cpf, Users)

    if User:
        print("\n=== Account created successfully! ===")
        return {"Agency": Agency, "AccountNumber": AccountNumber, "User": User}

    print("\n@@@ User not found, Account creation flow closed! @@@")

def listar_Accounts(Accounts):
    for Account in Accounts:
        Line = f"""\
            Agência:\t{Account['Agency']}
            C/C:\t\t{Account['AccountNumber']}
            Titular:\t{Account['User']['Name']}
        """
        print("=" * 100)
        print(textwrap.dedent(Line))

def main():
    Bound_Withdraw = 3
    Agency = "0001"

    Balance = 0
    Bound = 500
    BankStatement = ""
    NumberWithdraw = 0
    Users = []
    Accounts = []


    while True:

        Option = menu()

        if Option == "1":
            Value = float(input("Enter the Deposit Value: "))

            Balance, BankStatement = Put(Balance, Value, BankStatement)

        elif Option == "2":
           Value = float(input("Enter the Withdraw Value: ")) 

           Balance, BankStatement = Withdraw(
                Balance=Balance,
                Value=Value,
                BankStatement=BankStatement,
                Bound=Bound,
                NumberWithdraw=NumberWithdraw,
                Bound_Withdraw=Bound_Withdraw,
            )

        elif Option == "3":
           exibir_BankStatement(Balance, BankStatement=BankStatement) 

        elif Option == "4":
           CreateUser(Users)  

        elif Option == "5":
           AccountNumber = len(Accounts) + 1
           Account = CreateAccount(Agency, AccountNumber, Users)

           if Account:
               Accounts.append(Account)

        elif Option == "6":
           listar_Accounts(Accounts)        
    
        elif Option == "7":
           break    

        else:
           print("Invalid operation, please reselect the desired operation.")

main()   