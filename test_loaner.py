import unittest
import random
import datetime
from loaner import Item, Book, Game, VideoGame, UnloanableException, NotLoanedException


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
        self.assertRaises(UnloanableException, self.item.loan)

    def test_collect_method_fails_for_unloaned_items(self):
        self.assertRaises(NotLoanedException, self.item.collect)


class TestBook(unittest.TestCase):

    def setUp(self):
        self.pages = random.randint(50, 1000)
        self.cover = 'hardcover'
        self.book = Book(self.pages, self.cover)

    def test_pages_set_in_constructor(self):
        self.assertEqual(self.book.pages, self.pages)

    def test_cover_set_in_constructor(self):
        self.assertEqual(self.book.cover, self.cover)

    def test_mark_read_sets_read_variable(self):
        self.book.mark_read()
        self.assertTrue(self.book.read)


class TestGame(unittest.TestCase):

    def setUp(self):
        self.players = random.randint(1, 8)
        self.game = Game(self.players)

    def test_players_set_in_constructor(self):
        self.assertEqual(self.game.players, self.players)

    def test_mark_completed_sets_completed_variable(self):
        self.game.mark_completed()
        self.assertTrue(self.game.completed)


class TestVideoGame(unittest.TestCase):

    def setUp(self):
        self.players = random.randint(1, 8)
        self.platform = 'Xbox 360'
        self.game = VideoGame(self.players, self.platform)

    def test_platform_set_in_constructor(self):
        self.assertEqual(self.game.platform, self.platform)
