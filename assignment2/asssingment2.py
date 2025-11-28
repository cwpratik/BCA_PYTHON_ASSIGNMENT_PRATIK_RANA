"""
Name: Om Mathur
Roll No.: 2501201026
Project: Library Inventory & Borrowing System
"""

# ------------------------------
# GLOBAL DATA STORAGE
# ------------------------------
books = {}          # Stores all book records
borrowed = {}       # Stores borrowing info: {student: bookID}


# ------------------------------
# BONUS
# ------------------------------
def load_data():
    try:
        with open("books.csv", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    book_id, title, author, copies = parts
                    books[book_id] = {
                        "title": title,
                        "author": author,
                        "copies": int(copies)
                    }
    except FileNotFoundError:
        pass


def save_data():
    with open("books.csv", "w") as f:
        for book_id, data in books.items():
            f.write(f"{book_id},{data['title']},{data['author']},{data['copies']}\n")


# ------------------------------
# TASK 2: ADD BOOKS
# ------------------------------
def add_book():
    print("\n--- Add Book ---")
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    copies = int(input("Enter Number of Copies: "))

    books[book_id] = {
        "title": title,
        "author": author,
        "copies": copies
    }

    print("\nBook added successfully!")


# ------------------------------
# TASK 3: DISPLAY BOOKS
# ------------------------------
def view_books():
    print("\n--- Book List ---")
    print(f"{'ID':<10}{'Title':<25}{'Author':<20}{'Copies'}")
    print("-" * 60)

    if not books:
        print("No books available.")
        return

    for book_id, info in books.items():
        print(f"{book_id:<10}{info['title']:<25}{info['author']:<20}{info['copies']}")


# SEARCH FUNCTIONS
def search_by_id(book_id):
    return books.get(book_id, None)


def search_by_title(title_sub):
    results = []
    for book_id, info in books.items():
        if title_sub.lower() in info['title'].lower():
            results.append((book_id, info))
    return results


def search_book():
    print("\n--- Search Book ---")
    print("1. Search by Book ID")
    print("2. Search by Title")
    choice = input("Enter choice: ")

    if choice == "1":
        bid = input("Enter Book ID: ")
        result = search_by_id(bid)
        if result:
            print("\nBook Found!")
            print(result)
        else:
            print("\nBook Not Found.")

    elif choice == "2":
        title = input("Enter title to search: ")
        results = search_by_title(title)
        if results:
            print("\nBooks Found:")
            for book_id, data in results:
                print(book_id, " → ", data)
        else:
            print("\nNo matching books found.")


# ------------------------------
# TASK 4: BORROW BOOK
# ------------------------------
def borrow_book():
    print("\n--- Borrow Book ---")
    student = input("Enter Student Name: ")
    book_id = input("Enter Book ID: ")

    if book_id in books:
        if books[book_id]["copies"] > 0:
            books[book_id]["copies"] -= 1
            borrowed[student] = book_id
            print(f"\n{student} borrowed {book_id} successfully!")
        else:
            print("\nError: No copies available.")
    else:
        print("\nError: Book ID does not exist.")


# ------------------------------
# TASK 5: RETURN BOOK
# ------------------------------
def return_book():
    print("\n--- Return Book ---")
    student = input("Enter Student Name: ")
    book_id = input("Enter Book ID: ")

    if student in borrowed and borrowed[student] == book_id:
        books[book_id]["copies"] += 1
        del borrowed[student]
        print("\nBook returned successfully!")
    else:
        print("\nError: No matching borrow record found.")

    # List comprehension to show borrowed list
    borrowed_list = [f"{s} -> {b}" for s, b in borrowed.items()]
    print("\nCurrent Borrowed Books:")
    print(borrowed_list)


# ------------------------------
# MAIN MENU LOOP (TASK 1 + 6)
# ------------------------------
def menu():
    load_data()  # Bonus load

    while True:
        print("\n==============================")
        print("     LIBRARY MANAGER")
        print("==============================")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")
        print("==============================")

        option = input("Enter your choice: ")

        if option == "1":
            add_book()
        elif option == "2":
            view_books()
        elif option == "3":
            search_book()
        elif option == "4":
            borrow_book()
        elif option == "5":
            return_book()
        elif option == "6":
            save_data()  # Bonus save
            print("\nThank you for using Library Manager!")
            break
        else:
            print("\nInvalid choice, try again.")


# Run program
menu()