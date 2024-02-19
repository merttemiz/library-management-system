#!/usr/bin/env python
# coding: utf-8

# In[68]:


class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")
    
    def __del__(self):
        self.file.close()

    def list_books(self):
        counter = 0
        self.file.seek(0)
        books = self.file.readlines()
        if not books:
            print("There are no books in the library.")
        else:
            for book in books:
                counter += 1
                print("%d. Book:" % counter, book.strip())

    def add_book(self, title, author, release_year, pages):
        book_info = f"{title},{author},{release_year},{pages}\n"
        self.file.write(book_info)
        print(f"The book named {title} has been added to the library.")

    def remove_book(self, title):
        self.file.seek(0)
        books = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()
        removed = False
        for book in books:
            if title.lower() not in book.lower():
                self.file.write(book)
            else:
                removed = True
        if removed:
            print(f"The book named {title} has been removed from the library.")
        else:
            print(f"The book named {title} could not be found in library.")

def main():
    lib = Library()
    while True:
        print("\n*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("q) Quit")
        choice = input("Please make your choice: ")
        if choice == "1":
            lib.list_books()
        elif choice == "2":
            title = input("Please enter the book name: ")
            author = input("Author: ")
            release_year = input("Release Year: ")
            pages = input("Number of Pages: ")
            lib.add_book(title, author, release_year, pages)
        elif choice == "3":
            title = input("Please enter the book name that you want to delete: ")
            lib.remove_book(title)
        elif choice.lower() == "q":
            print("You have logged out of the program.")
            break
        else:
            print("Invalid choice, please make another one.")

if __name__ == "__main__":
    main()


# In[ ]:




