from Util.DBconnection import DBConnection
from Interface.ICustomerServices import ICustomerServices
from Exceptions.CustomerExceptions import InsufficientbalanceError, NoLoansAvailableError, NoHistoryAvailableError

class CustomerServices(DBConnection, ICustomerServices):
    def get_account(self, user_id):
        try:
            self.cursor.execute("SELECT AccountNumber FROM Accounts WHERE UserID = ?", (user_id),)
            account_number = self.cursor.fetchall()
            return account_number
        except Exception as e:
            print(e)
    
    def deposit(self, AccountNumber, Amount):
        try:
            self.cursor.execute("SELECT Balance FROM Accounts WHERE AccountNumber = ?", (AccountNumber),)
            balance = self.cursor.fetchall()
            balance += Amount
            self.cursor.execute("UPDATE Accounts SET Balance = ? WHERE AccountNumber = ?",(balance, AccountNumber),)
            self.conn.commit()
        except Exception as e:
            print(e)

    def withdrawl(self, AccountNumber, Amount):
        try:
            self.cursor.execute("SELECT Balance FROM Accounts WHERE AccountNumber = ?", (AccountNumber),)
            balance = self.cursor.fetchall()
            if balance >= Amount:
                balance -= Amount
                self.cursor.execute("UPDATE Accounts SET Balance = ? WHERE AccountNumber = ?",(balance, AccountNumber),)
                self.conn.commit()
            else:
                raise InsufficientbalanceError
        except Exception as e:
            print(e)

    def check_balance(self, AccountNumber):
        try:
            self.cursor.execute("SELECT Balance FROM Accounts WHERE AccountNumber = ?", (AccountNumber),)
            balance = self.cursor.fetchall()
            return balance
        except Exception as e:
            print(e)

    def view_loans(self, AccountNumber):
        try:
            self.cursor.execute("SELECT * FROM Loans WHERE AccountNumber = ?", (AccountNumber),)
            loans = self.cursor.fetchall()
            if len(loans)>0:
                return loans
            else:
                raise NoLoansAvailableError
        except Exception as e:
            print(e)

    def transaction_history(self, AccountNumber):
        try:
            self.cursor.execute("SELECT * FROM Transactions WHERE AccountNumber = ?", (AccountNumber),)
            history = self.cursor.fetchall()
            if len(history)>0:
                return history
            else:
                raise NoHistoryAvailableError
        except Exception as e:
            print(e)