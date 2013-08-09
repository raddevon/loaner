import datetime

"""
Tracks items loaned out to friends
"""


def except_unloanable(func):
    def inner(self, *args, **kwargs):
        if not self.loanable:
            raise TypeError('This item cannot be loaned.')
        else:
            return func(self, *args, **kwargs)
    return inner


class Item(object):

    def __init__(self, loanable=True):
        self.loanable = loanable
        self.loaned = False

    @except_unloanable
    def loan(self, borrower=None, date=datetime.datetime.now()):
        self.loaned = True
        self.borrower = borrower
        self.loan_date = date

    @except_unloanable
    def collect(self, borrower=None, date=datetime.datetime.now()):
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
