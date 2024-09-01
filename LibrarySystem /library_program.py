import datetime 

class LibrarySystem:
    def __init__(self, name):
        # Constructor for the LibrarySystem class
        # initializes the library with a name and an empty dictionary to store books
        self.name = name
        self.books = {}

    def add_book(self, title, author):
        # adds a new book to the library if it doesn't already exist
        if title not in self.books:
            self.books[title] = {"author": author, "is_borrowed": False, "borrowed_date": None}
            print(f"Book titled {title} has been added to the library.")
        else:
            print(f"Book titled {title} already exists and cannot be added again.")

    def remove_book(self, title):
        # removes an existing book from the library if it exists
        if title in self.books:
            del self.books[title]
            print(f"Book titled {title} has been removed from the library.")
        else:
            print(f"Book titled {title} does not exist.")

    def borrow_book(self, title):
        # marks a book as borrowed if it's available
        if title in self.books:
            if not self.books[title]["is_borrowed"]:
                self.books[title]["is_borrowed"] = True
                self.books[title]["borrowed_date"] = datetime.datetime.now()
                print(f"Book titled {title} is now borrowed and needs to be returned within 14 days.")
            else:
                print(f"The book titled {title} is already borrowed by someone.")
        else:
            print(f"Book titled {title} does not exist in this library :(")

    def return_book(self, title):
        # marks a book as returned and checks for overdue days
        if title in self.books:
            if self.books[title]["is_borrowed"]:
                borrowed_date = self.books[title]["borrowed_date"]
                overdue_days = self.calculate_overdue_days(borrowed_date)
                print(f"Book titled {title} has been returned.")
                self.books[title]["is_borrowed"] = False
                self.books[title]["borrowed_date"] = None

                if overdue_days > 0:
                    print(f"The book is {overdue_days} days late, and a punitive fee will be administered.")
            else:
                print(f"The book titled {title} is currently not borrowed and thus cannot be returned.")
        else:
            print(f"Book titled {title} does not exist in this library.")

    def is_available(self, title):
        # checks if a book is available for borrowing
        if title in self.books:
            if not self.books[title]["is_borrowed"]:
                print(f"Book titled {title} is available for borrowing.")
                return True
            else:
                print(f"Book titled {title} is not available for borrowing.")
                return False
        else:
            print(f"Book titled {title} does not exist in this library :(")
            return False

    def print_available_titles(self):
        # prints all available titles in the library
        available_titles = [title for title, book_info in self.books.items() if not book_info["is_borrowed"]]
        print("Available titles:", available_titles)
        return available_titles

    def calculate_overdue_days(self, borrowed_date):
        # calculates the number of days a book is overdue
        due_date = borrowed_date + datetime.timedelta(days=14)
        # returns the number of overdue days or 0 if the book is not overdue
        return max(0, (datetime.datetime.now() - due_date).days)




# example usage of the LibrarySystem class
print("\n")
library = LibrarySystem("My Library")
library.add_book("Atomic Habits", "James Clear")
library.add_book("Project Management", "Greg Horine")

print("\nAdding book..")
library.add_book("Salesforce for Dummies", "Jon Paz")

print("\nRemoving book..")
library.remove_book("Salesforce for Dummies")

print("\nBorrowing book..")
library.borrow_book("Atomic Habits")

print("\nReturning book..")
library.return_book("Atomic Habits")

print("\nChecking book availability..")
library.is_available("Project Management")

print("\nChecking all available books in the library..")
library.print_available_titles()
