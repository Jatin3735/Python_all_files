from datetime import datetime

class Account:
    def __init__(self,acc,bal):
        self.acc_id= acc
        self.balance= bal
        self.transactions = []
        self.transactions.append(f"{datetime.now()} -- Account openend with bonus Rs.{bal}  | Balance : {self.balance}")
    
    def debit(self,amount):
        if amount <=0:
            print("Invalid amount. Please enter amount greater than zero.")
        elif amount > self.balance:
            print("You don't have enough money.")
        else:
            self.balance -= amount
            self.transactions.append(f"{datetime.now()} - Debited Rs.{amount} | Balance : {self.balance}")
            print(f"Debited {amount}. New Balance is {self.get_balance()}")

    def credit(self,amount):
        if amount <=0:
            print("Invalid amount. Please enter amount greater than zero.")
        else:
            self.balance += amount
            self.transactions.append(f"{datetime.now()} - Credited Rs.{amount} | Balance : {self.balance}")
            print(f"Credited {amount}. New Balance is {self.get_balance()}")

    def get_balance(self):
        print(f"Account {self.acc_id} Balance : {self.balance}")
        return self.balance

    def tr_history(self):
        print("\n-----Transaction History-----")
        if not self.transactions:
            print("No Transaction yet.")
        else:
            for transaction in self.transactions:
                print(transaction)
        print("--------------------------------")

def main():
    bonus_bal = 1000
    while True:
        acc_id = input("Enter Account ID : ")
        if len(acc_id) < 5:
            print("Account ID must be at least 5 character.")
        else:
            break

    account = Account(acc_id,bonus_bal)
    print(f"\n🎉 You get bonus of Rs.{bonus_bal} at opening your account first time.")

    while True:
        print("\n======Menu======")
        print("1. Debit")
        print("2. Credit")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter you choice : (1/2/3/4/5):")

        if choice =='1':
            amount = float(input("Enter amount to Debit : "))
            account.debit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to Credit : "))
            account.credit(amount)
        elif choice == '3':
            account.get_balance()
        elif choice == '4':
            account.tr_history()
        elif choice == '5':
            print("Exiting the program......\nThank You")
            break
        else:
            print("Invalid Choice. Please select choice between 1 to 5.")
    
if __name__ == "__main__":
    main()




            


    