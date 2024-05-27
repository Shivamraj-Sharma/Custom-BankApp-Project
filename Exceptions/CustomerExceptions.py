class InsufficientbalanceError(Exception):
    def __init__(self):
        super().__init__("\t\t !!! Insufficient Balance !!!")

class NoLoansAvailableError(Exception):
    def __init__(self):
        super().__init__("\t\t !!! No loans to display !!!")

class NoHistoryAvailableError(Exception):
    def __init__(self):
        super().__init__("\t\t !!! No transaction history to display !!!")