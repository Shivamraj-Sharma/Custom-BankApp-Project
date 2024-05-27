from Util.DBconnection import DBConnection
from Interface.IAdminServices import IAdminServices
from Exceptions.AdminExceptions import NoSuchAccountError, NoTrasactionHistoryError, NoLoanAvailableError

class AdminServices(DBConnection, IAdminServices):
    def create_account(self, Accounts):
        try:
            self.cursor.execute("INSERT INTO Accounts (AccountNumber, UserID, Balance) VALUES (?, ?, ?)",(Accounts.AccountNumber, Accounts.UserID, Accounts.Balance),)
            self.conn.commit()
            print("\n\t\t...Account Created Sucessfully...")
        except Exception as e:
            print(e)
    
    def delete_account(self, AccountNumber):
        try:
            self.cursor.execute("SELECT * FROM Accounts WHERE AccountNumber = ?", (AccountNumber),)
            account = self.cursor.fetchall()
            if len(account)>0:
                self.cursor.execute("DELETE FROM Accounts WHERE AccountNumber = ?", (AccountNumber),)
                self.conn.commit()
                print("\n\t\t...Account Deleted Sucessfully...")
            else:
                raise NoSuchAccountError
        except Exception as e:
            print(e)

    def view_accounts(self):
        try:
            self.cursor.execute("SELECT * FROM Accounts")
            Accounts = self.cursor.fetchall()
            return Accounts
        except Exception as e:
            print(e)

    def transaction_by_date(self, startDate, EndDate):
        try:
            self.cursor.execute("SELECT * FROM Transactions WHERE TransactionDate >= ? AND TransactionDate <= ?", (startDate, EndDate),)
            Transactions = self.cursor.fetchall()
            if len(Transactions)>0:
                return Transactions
            else:
                raise NoTrasactionHistoryError
        except Exception as e:
            print(e)

    def transaction_by_account(self, AccountNumber):
        try:
            self.cursor.execute("SELECT * FROM Transactions WHERE AccountNumber = ?", (AccountNumber),)
            Transactions = self.cursor.fetchall()
            if len(Transactions)>0:
                return Transactions
            else:
                raise NoTrasactionHistoryError
        except Exception as e:
            print(e)

    def transaction_by_type(self, type):
        try:
            self.cursor.execute("SELECT * FROM Transactions WHERE TransactionType = ?", (type),)
            Transactions = self.cursor.fetchall()
            if len(Transactions)>0:
                return Transactions
            else:
                raise NoTrasactionHistoryError
        except Exception as e:
            print(e)

    def generate_loan(self, Loans):
        try:
            self.cursor.execute("INSERT INTO Loans (LoanID, UserID, AccountNumber, LoanType, Amount, InterestRate, Duration) VALUES (?, ?, ?, ?, ?, ?, ?)",(Loans.LoanID, Loans.UserID, Loans.AccountNumber, Loans.LoanType, Loans.Amount, Loans.InterestRate, Loans.Duration),)
            self.conn.commit()
            print("\n\t\t...Loan Granted Sucessfully...")
        except Exception as e:
            print(e)

    def view_loans(self):
        try:
            self.cursor.execute("SELECT * FROM Loans")
            Loans = self.cursor.fetchall()
            return Loans
        except Exception as e:
            print(e)

    def loan_by_account(self, AccountNumber):
        try:
            self.cursor.execute("SELECT * FROM Loans WHERE AccountNumber = ?", (AccountNumber),)
            Loans = self.cursor.fetchall()
            if len(Loans)>0:
                return Loans
            else:
                raise NoLoanAvailableError
        except Exception as e:
            print(e)