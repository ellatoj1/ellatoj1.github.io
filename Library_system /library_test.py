import unittest  # unittest module for creating and running tests
import datetime  
from library_program import LibrarySystem  # importing the LibrarySystem class from library_program.py

class TestLibrarySystem(unittest.TestCase):
    # Test case for adding an existing book to the library
    def test_add_existing_book(self):
        print('\n')
        print("Testing adding EXISTING book:")
        library = LibrarySystem("Test Library")
        library.add_book("Atomic Habits", "James Clear")
        library.add_book("Project Management", "Greg Horine")
        # attempt to add the same books again
        library.add_book("Atomic Habits", "James Clear")
        library.add_book("Project Management", "Greg Horine")
        # verify that the library still only contains two unique books
        self.assertEqual(len(library.books), 2)

    # Test case for adding a new book to the library
    def test_add_new_book(self):
        print('\n')
        print("Testing adding NEW book:")
        library = LibrarySystem("Test Library")
        library.add_book("Pojken och Tigern", "Lars Westman")
        # verify that the new book is added to the library's collection
        self.assertTrue("Pojken och Tigern" in library.books)

    # Test case for removing an existing book from the library
    def test_remove_book(self):
        print('\n')
        print("Testing REMOVING existing book:")
        library = LibrarySystem("Test Library")
        library.add_book("Atomic Habits", "James Clear")
        library.remove_book("Atomic Habits")
        # verify that the book has been removed from the library's collection
        self.assertFalse("Atomic Habits" in library.books)

    # Test case for borrowing a book from the library
    def test_borrow_book(self):
        print('\n')
        print("Testing BORROWING book:")
        library = LibrarySystem("Test Library")
        library.add_book("Pojken och Tigern", "Lars Westman")
        library.borrow_book("Pojken och Tigern")
        # verify that the book is marked as borrowed
        self.assertTrue(library.books["Pojken och Tigern"]["is_borrowed"])

    # Test case for returning a book on time
    def test_return_book_on_time(self):
        print('\n')
        print("Testing RETURNING book ON TIME:")
        library = LibrarySystem("Test Library")
        library.add_book("Pojken och Tigern", "Lars Westman")
        library.borrow_book("Pojken och Tigern")
        library.return_book("Pojken och Tigern")
        # verify that the book is no longer marked as borrowed
        self.assertFalse(library.books["Pojken och Tigern"]["is_borrowed"])

    # Test case for returning a book late
    def test_return_book_late(self):
        print('\n')
        print("Testing RETURNING book LATE:")
        library = LibrarySystem("Test Library")
        library.add_book("Pojken och Tigern", "Lars Westman")
        library.borrow_book("Pojken och Tigern")
        # manually set the borrowed date to simulate a late return
        library.books["Pojken och Tigern"]["borrowed_date"] = datetime.datetime.now() - datetime.timedelta(days=20)
        library.return_book("Pojken och Tigern")
        # verify that the book is no longer marked as borrowed
        self.assertFalse(library.books["Pojken och Tigern"]["is_borrowed"])

    # Test case for checking if a book is available for borrowing
    def test_is_available(self):
        print('\n')
        print("Testing if book is AVAILABLE:")
        library = LibrarySystem("Test Library")
        library.add_book("Atomic Habits", "James Clear")
        # verify that the book is available for borrowing
        self.assertTrue(library.is_available("Atomic Habits"))

    # Test case for checking if a book is not available for borrowing
    def test_is_not_available(self):
        print('\n')
        print("Testing if book is NOT AVAILABLE:")
        library = LibrarySystem("Test Library")
        library.add_book("Atomic Habits", "James Clear")
        library.borrow_book("Atomic Habits")
        # verify that the book is not available for borrowing
        self.assertFalse(library.is_available("Atomic Habits"))

    # Test case for printing all available book titles
    def test_print_available_titles(self):
        print('\n')
        print("Testing ALL AVAILABLE titles:")
        library = LibrarySystem("Test Library")
        library.add_book("Atomic Habits", "James Clear")
        library.add_book("Project Management", "Greg Horine")
        library.borrow_book("Atomic Habits")
        available_titles = library.print_available_titles()
        # verify that the borrowed book is not in the list of available titles
        self.assertNotIn("Atomic Habits", available_titles)
        # verify that the non-borrowed book is in the list of available titles
        self.assertIn("Project Management", available_titles)

if __name__ == '__main__':
    unittest.main()
