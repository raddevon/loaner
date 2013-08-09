import datetime

"""
Tracks items loaned out to friends
"""


class UnloanableException(Exception):
    pass


class NotLoanedException(Exception):
    pass


class Item(object):

    def __init__(self, loanable=True):
        self.loanable = loanable
        self.loaned = False

    def loan(self, borrower=None, date=datetime.datetime.now()):
        if not self.loanable:
            raise UnloanableException('Item cannot be loaned.')
        self.loaned = True
        self.borrower = borrower
        self.loan_date = date

    def collect(self, borrower=None, date=datetime.datetime.now()):
        if not self.loaned:
            raise NotLoanedException('This item is not currently loaned out.')
        self.loaned = False
        self.return_date = date


class Book(Item):

    def __init__(self, pages, cover):
        super(Item, self).__init__()
        self.pages = pages
        self.cover = cover

    def mark_read(self):
        self.read = True


class Game(Item):

    def __init__(self, players):
        super(Item, self).__init__()
        self.players = players

    def mark_completed(self):
        self.completed = True


class VideoGame(Game):

    def __init__(self, players, platform):
        super(Game, self).__init__()
        self.platform = platform
