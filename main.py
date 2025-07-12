class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account = acc
        self.transactions = []

    def debit(self,amount):
        if amount > self.balance:
            print("You do not have enough money to perform this transaction")
        else:
            self.balance -=amount
            self.transactions.append(f"Debited Rs.{amount}")
            print(f"Rs.{amount} was debited")
            print(f"Total Balance is = Rs.{self.get_balance()} ")


    def credit(self,amount):
        if amount > 1000000:
             print("Out of limits!!  You have store minimum than 10 lakh.\nIf you want to store more money you will be open another account ")
        else:
            self.balance +=amount
            self.transactions.append(f"Credited Rs.{amount}")
            print(f"Rs.{amount} was debited")
            print(f"Total Balance is = Rs.{self.get_balance()}")


    def get_balance(self):
        return self.balance
    
    def show_tr_history(self):
        if self.transactions:
            print("\nTransaction History:")
            for transaction in self.transactions:
                print(transaction)
        else:
            print("No Transaction yet.")
    

def details():
    acc_balance = 1000
    acc_id = input("Enter your Account ID: ")

    while len(acc_id)<5:
        print("Account ID must be at least 5 characters")
        acc_id = input("Enter your Account ID: ")


    account = Account(acc_balance,acc_id)

    print(f"You get Bonus of Rs.{acc_balance} for opening your account first time ")


    while True:
        print("\nChoose an operation: ")
        print("1. Debit")
        print("2. Credit")
        print("3. View Balance")
        print("4. View Transaction History")
        print("5. Exit")

        choice = input("Enter your Choice (1/2/3/4): ")

        if choice == '1':
            try:
                amount = float(input("Enter the amount to Debit Rs. "))
                account.debit(amount)
            except ValueError:
                print("Invalid input! Please select a numeric value.")

        elif choice == '2':
            try:
                amount = float(input("Enter the amount to Credit Rs. "))
                account.credit(amount)
            except ValueError:
                print("Invalid input! Please select a numeric value.")
        
        elif choice == '3':
            print(f"Current Balance is Rs.{account.get_balance()}")

        elif choice == '4':
            account.show_tr_history()

        elif choice == '5':
            print("Exiting the program....")
            break
        else:
            print("Invalid Choice! Please select again")


details()