class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}. New balance: {self.__balance}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the current balance.")

    def __display_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return self.__display_balance()

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
            print(f"Balance updated to: {self.__balance}")
        else:
            print("Error: Balance cannot be negative.")

    def display_account_info(self):
        print(f"Account Number: {self.get_account_number()}")
        print(f"Current Balance: {self.get_balance()}")


if __name__ == "__main__":
    
    account = BankAccount("123456789", 100.0)

    
    account.deposit(50.0)

    
    account.withdraw(30.0)

    
    account.set_balance(-20.0)

    
    account.display_account_info()
