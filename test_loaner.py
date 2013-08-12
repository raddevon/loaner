import unittest
import random
import datetime
from loaner import Item, Book, Game, VideoGame, UnloanableError, NotLoanedError


class TestItem(unittest.TestCase):

    def setUp(self):
        self.item = Item()

    def test_new_item(self):
        self.assertIsInstance(self.item, Item)

    def test_loan_method_sets_loaned_variable(self):
        self.item.loan()
        self.assertTrue(self.item.loaned)

    def test_sets_borrower_on_loan(self):
        self.item.loan(borrower='James')
        self.assertEqual(self.item.borrower, 'James')

    def test_sets_loan_date(self):
        self.loan_date = datetime.datetime.now()
        self.item.loan(date=self.loan_date)
        self.assertEqual(self.item.loan_date, self.loan_date)

    def test_sets_return_date(self):
        self.item.loan()
        self.return_date = datetime.datetime.now()
        self.item.collect(date=self.return_date)
        self.assertEqual(self.item.return_date, self.return_date)


class TestUnloanableItem(unittest.TestCase):

    def setUp(self):
        self.item = Item(False)

    def test_loanable_is_false(self):
        self.assertFalse(self.item.loanable)

    def test_loan_method_fails_for_unloanable_items(self):
        self.assertRaises(UnloanableError, self.item.loan)

    def test_collect_method_fails_for_unloaned_items(self):
        self.assertRaises(NotLoanedError, self.item.collect)


class TestBook(TestItem):

    def setUp(self):
        self.pages = random.randint(50, 1000)
        self.cover = 'hardcover'
        self.item = Book(self.pages, self.cover)

    def test_pages_set_in_constructor(self):
        self.assertEqual(self.item.pages, self.pages)

    def test_cover_set_in_constructor(self):
        self.assertEqual(self.item.cover, self.cover)

    def test_mark_read_sets_read_variable(self):
        self.item.mark_read()
        self.assertTrue(self.item.read)


class TestGame(TestItem):

    def setUp(self):
        self.players = random.randint(1, 8)
        self.item = Game(self.players)

    def test_players_set_in_constructor(self):
        self.assertEqual(self.item.players, self.players)

    def test_mark_completed_sets_completed_variable(self):
        self.item.mark_completed()
        self.assertTrue(self.item.completed)


class TestVideoGame(TestGame):

    def setUp(self):
        self.players = random.randint(1, 8)
        self.platform = 'Xbox 360'
        self.item = VideoGame(self.players, self.platform)

    def test_platform_set_in_constructor(self):
        self.assertEqual(self.item.platform, self.platform)
