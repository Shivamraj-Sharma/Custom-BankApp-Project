class NoSuchAccountError(Exception):
    def __init__(self):
        super().__init__("\t\t !!! No Such Account !!!")

class NoTrasactionHistoryError(Exception):
    def __init__(self):
        super().__init__("\t\t !!! No transaction history to display !!!")

class NoLoanAvailableError(Exception):
    def __init__(self):
        super().__init__("\t\t !!! No loans to display !!!")