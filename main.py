import os

class Library:

    def __init__(self, books_file):
        self.books_file = books_file

        while True:
            user_input = input(
                "Would you like to 'List Books', 'Add Book', 'Remove Book', or 'Quit'? You can write your request: ").lower()

            valid_options = ["add book", "list books", "remove book", "quit"]

            if user_input in valid_options:
                if user_input == "add book":
                    self.add_book()
                elif user_input == "list books":
                    self.list_books()
                elif user_input == "remove book":
                    self.remove_book()
                else:
                    exit()
            else:
                print("Invalid input. Please choose one of the listed options.")

    def add_book(self):
        book_name = input("Enter the book's name you want to add: ")
        book_author = input("Enter the book's author: ")
        book_rel_year = input("Enter book's release year: ")
        book_num_page = input("Enter book's number of pages: ")

        book_info = f"{book_name}, Author: {book_author}, Release Year: {book_rel_year}, Number of Pages: {book_num_page}"

        with open(self.books_file, 'a') as file:
            file.write(book_info + '\n')

        print(f"{book_name} has been added to your library.")

    def list_books(self):
        with open(self.books_file, 'r') as file:
            print(file.read())

    def remove_book(self):
        remove_book = input("Enter the title of the book you want to remove: ").strip()
        found = False

        with open(self.books_file, 'r') as input_file, open("temp.txt", 'w') as output_file:
            for line in input_file:
                if not line.strip("\n").startswith(remove_book):
                    output_file.write(line)
                else:
                    found = True

        if found:
            os.replace('temp.txt', self.books_file)
            print(f"{remove_book} has been successfully removed.")
        else:
            print(f"Book '{remove_book}' not found in your library.")

my_library = Library("books.txt")
