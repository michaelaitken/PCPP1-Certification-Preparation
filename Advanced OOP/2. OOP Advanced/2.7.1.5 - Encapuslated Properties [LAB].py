'''
Objectives

    improving the student's skills in operating with the getter, setter, and deleter methods;
    improving the student's skills in creating their own exceptions.

Scenario

    Implement a class representing an account exception,
    Implement a class representing a single bank account,
    This class should control access to the account number and account balance attributes by implementing the properties:
        it should be possible to read the account number only, not change it. In case someone tries to change the account number, raise an alarm by raising an exception;
        it should not be possible to set a negative balance. In case someone tries to set a negative balance, raise an alarm by raising an exception;
        when the bank operation (deposit or withdrawal) is above 100.000, then additional message should be printed on the standard output (screen) for auditing purposes;
        it should not be possible to delete an account as long as the balance is not zero;
    test your class behavior by:
        setting the balance to 1000;
        trying to set the balance to -200;
        trying to set a new value for the account number;
        trying to deposit 1.000.000;
        trying to delete the account attribute containing a non-zero balance.
'''

class AccountExecption(Exception):
    pass

class Account:
    def __init__(self, number) -> None:
        self.__account_number = number
        self.__account_balance = 0
    
    # Account Number Property Methods
    @property    
    def account_number(self):
        return self.__account_number
    
    @account_number.setter
    def account_number(self, _):
        raise AccountExecption("Cannot change Account Number!")        
    
    @account_number.deleter
    def account_number(self):
        if self.__account_balance > 0:
            raise AccountExecption("Cannot delete Account. Balance not Zero")
        else:
            del self.__account_number
    
    # Account Balance Property Methods
    @property
    def account_balance(self):
        return self.__account_balance
    
    @account_balance.setter
    def account_balance(self, value):
        if value >= 0:
            self.__account_balance = value
        else:
            raise AccountExecption("Account Balance cannot be negative!")
    
    # Audit Decorator Function
    def audit_message(function):
        def wrappper(self, amount):
            if amount > 100000:
                print("Transaction over $100,000")
            function(self, amount)
        return wrappper
    
    # Other Methods
    @audit_message
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
        else:
            raise AccountExecption("Deposit amount cannot be negative")
    
    @audit_message
    def withdraw(self, amount):
        if amount <= 0:
            raise AccountExecption("Withdraw amount cannot be negative")
        elif amount > self.__account_balance:
            raise AccountExecption("Insufficient Funds!")
        else:
            self.__account_balance -= amount

# === TESTING ===

account1 = Account(123456)

account1.account_balance = 1000

try:
    account1.account_balance = -200
except AccountExecption:
    print("$-200 Account Balance Failed!")

try:
    account1.account_number = 123
except AccountExecption:
    print("Setting Account Number Failed!")

account1.deposit(1000000)

# NOTE(MIKE): Learn how to prevent deleting an object manually, until a condition is met. (if it is possible)
# Instead, here is the same but for Account Number instead
try:
    del account1.account_number
except AccountExecption:
    print("Account Number deletation failed!")
