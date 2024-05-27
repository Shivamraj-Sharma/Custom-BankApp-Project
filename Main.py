from DAO.CommonServices import CommonServices
from DAO.CustomerServices import CustomerServices
from DAO.AdminServices import AdminServices
from Entity.Accounts import Accounts
from Entity.Loans import Loans
from datetime import datetime

class Admin_Menu:
    admin_services = AdminServices()
    def admin_menu(self):
        while True:
            print(
                """   
                1. Create account
                2. Delete account   
                3. View all accounts
                4. View all transactions by date range
                5. View all transactions by account number
                6. View all transactions by type
                7. Generate loan
                8. View all loans
                9. View loans by account number
                0. Return to login page
                    """
            )
            choice = int(input("Please choose from above options: "))
            if choice == 1:
                AccountNumber = int(input("Enter account number: "))
                UserID = int(input("Enter user id: "))
                Balance = int(input("Enter balance: "))
                Account = Accounts(AccountNumber, UserID, Balance)
                self.admin_services.create_account(Account)
            if choice == 2:
                AccountNumber = int(input("Enter account number: "))
                self.admin_services.delete_account(AccountNumber)
            if choice == 3:
                accounts = self.admin_services.view_accounts()
                print(accounts)
            if choice == 4:
                startDate = datetime.strptime(input("Enter Start Date (DD-MM-YYYY): "), '%d-%m-%Y')
                endDate = datetime.strptime(input("Enter End Date (DD-MM-YYYY): "), '%d-%m-%Y')
                transactions = self.admin_services.transaction_by_date(startDate, endDate)
                print(transactions)
            if choice == 5:
                AccountNumber = int(input("Enter account number: "))
                transactions = self.admin_services.transaction_by_account(AccountNumber)
                print(transactions)
            if choice == 6:
                type = input("Enter transaction type: ")
                transactions = self.admin_services.transaction_by_type(type)
                print(transactions)
            if choice == 7:
                LoanID = int(input("Enter loan id: "))
                UserID = int(input("Enter user id: "))
                AccountNumber = int(input("Enter account number: "))
                LoanType = input("Enter loan type: ")
                Amount = int(input("Enter Amount: "))
                InterestRate = float(input("Enter interest rate: "))
                Duration = int(input("Enter loan duration: "))
                Loan = Loans(LoanID, UserID, AccountNumber, LoanType, Amount, InterestRate, Duration)
                self.admin_services.generate_loan(Loan)
            if choice == 8:
                loans = self.admin_services.view_loans()
                print(loans)
            if choice == 9:
                AccountNumber = int(input("Enter account number: "))
                loans = self.admin_services.loan_by_account(AccountNumber)
                print(loans)
            if choice == 0:
                self.close()
                break

class Customer_Menu:
    customer_service = CustomerServices()
    def customer_menu(self, UserID):
        user_id = UserID
        account_number = self.customer_service.get_account(user_id)
        while True:
            print(
                """      
                1. Deposit
                2. Withdrawl 
                3. Check Balance
                4. View loans 
                5. View transaction history
                0. Return to login page
                """
            )
            choice = int(input("Please choose from above options: "))
            if choice == 1:
                amount = int(input("Enter amount: "))
                self.customer_service.deposit(account_number, amount)
            if choice == 2:
                amount = int(input("Enter amount: "))
                self.customer_service.withdrawl(account_number, amount)
            if choice == 3:
                balance = self.customer_service.check_balance(account_number)
                print(f"Your account balance is: {balance}")
            if choice == 4:
                loans = self.customer_service.view_loans(account_number)
                print(loans)
            if choice == 5:
                history = self.customer_service.transaction_history(account_number)
                print(history)
            if choice == 0:
                self.close()
                print("\n\t\t!!! Thank You for using our Services !!!")
                break  

def main():
    Common_services = CommonServices()
    Admin_menu = Admin_Menu()
    Customer_menu = Customer_Menu()
    while True:
        print("\t\t !!! Welcome to MyBank !!!\n")
        LoginID = input("Enter your ID: ")
        Password = input("Enter your password: ")
        
        if Common_services.authenticate(LoginID, Password):
            if Common_services.check_role(LoginID) == "A":
                Admin_menu.admin_menu()
            else:
                UserID = int(Common_services.check_role(LoginID))
                Customer_menu.customer_menu(UserID)
        else:
            print("\t\t !!! Invalid Credentials !!!")
            print("\t\t     !!! Try Again !!!\n")

if __name__ == '__main__':
    main()