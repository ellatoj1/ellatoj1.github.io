# Library Management System

## Overview

This project implements a Library Management System that allows a librarian to efficiently manage the library's book inventory, handle book loans and returns, and track overdue books. It also includes comprehensive testing to ensure that all functionalities work as expected.

## Ultimate User Story

### **As a Librarian**, I want to manage the entire library's book lending system so that I can effectively administer the available books, register loans and returns, and keep track of overdue books.

- **Acceptance Criteria:**
  - **Add and Remove Books:**
    - The system should allow the librarian to add new books with the title and author to the library's database.
    - The system should allow the removal of a specific book from the system and confirm this by printing a notification.
  - **Manage Loans and Returns:**
    - The system should allow the librarian to mark a book as loaned out and record the loan date.
    - The system should allow a book to be marked as returned and calculate if the book is overdue, and if so, by how many days.
    - A confirmation should be printed for both loaning and returning books.
  - **View and Check Book Status:**
    - The system should allow the librarian to search for a specific book and get information about its availability.
    - The system should be able to list all available (not loaned out) books and print this list.

### **As a Developer**, I want to build and test the library system to ensure that all functionalities work according to the specification and that the system is stable and reliable.

- **Acceptance Criteria:**
  - **System Implementation:**
    - The system should be implemented with a class that handles the library's books and its functions as described above.
    - The books stored in the system should include the title, author, and information on whether they are loaned out, as well as the loan date when loaned out.
  - **Testing:**
    - A complete set of test cases should be included for each function in the system, verifying that the functions for adding, removing, loaning, returning, and calculating overdue days work correctly.
    - The tests should cover scenarios where books are added, removed, marked as loaned, returned, and where overdue calculations are performed and managed.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/library-management-system.git

