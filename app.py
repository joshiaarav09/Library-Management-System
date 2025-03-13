import sys


class User:
    def __init__(self,username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def __str__(self):
        pass


class Librarian(User):
    def __init__(self,username,password):
        super().__init__(username,password,role='Librarian')

    def add_books(self,book_id,book_name,author,genre):
        pass


class Student(User):
    def __init__(self,username,password):
        super().__init__(username,password,role='Student')


class Faculty(User):
    def __init(self, username,password):
        super().__init__(username,password,role='Faculty')


class Book:
    def __init__(self,book_id,book_name,author,genre):
        self.book_id = book_id
        self.book_name = book_name
        self.author = author
        self.genre = genre


class LibraryManagementSystem:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.logged_in_user = None

    def register_user(self,username,password, role='librarian'):
        role = role.lower()

        if username in self.users:
            print("Invalid!! User already registered!!!")
            return

        if not self.validate_role(role):
            return

        if role == 'librarian':
            user = Librarian(username,password)
        elif role == 'faculty':
            user = Faculty(username, password)
        elif role == 'student':
            user = Student(username,password)
        else:
            print("Invalid role. Please select from (librarian/student/faculty).")
            return

        self.users[username] = user
        print(f"User '{username}' registered successfully as {role}.")

    def login(self,username,password,role):
        if username not in self.users and self.users[username].password != password:
            print("Invalid Username or Password!! Try Again!!")
            return False

        self.logged_in_user = self.users[username]
        print(f"Welcome, {self.logged_in_user.username}! You are logged in as a {self.logged_in_user.role}.")
        return True

    def add_book(self):
        # Taking details of the book while adding
        book_id = input("Enter ID of the Book ")
        title = input("Enter title of the Book ")
        author = input("Enter name of the author of the book ")
        genre = input("Enter the Genre of the Book ")

        self.books[book_id] = Book(book_id,title,author,genre)
        print(f"{title} book added successfully!!!!")

    def update_book(self,books):
        book_id = input("Enter ID of the book you want to update: ")
        title = input("Enter the title of the book: ")
        author = input("Enter the author's name: ")
        genre = input("Enter the genre: ")

        if book_id in books:
            if title:
                books[book_id].title = title
            if author:
                books[book_id].author = author
            if genre:
                books[book_id].genre = genre
            print(f"Book with ID {book_id} changed successfully!!!!")
        else:
            print(f"Book with ID {book_id} not found!!!!!")

    def validate_role(self,role):
        valid_roles = ['librarian', 'faculty', 'student']
        if role.lower() not in valid_roles:
            print("Invalid Role Selection!!!! ")
            return False
        return True

    # Starting menu which the user will get while running LMS
    def menu(self):
        print("Welcome to Library Management System!!!!\n")
        while True:
            role = input("Enter your Role(librarian/faculty/student) or type 'exit' to quit:: ").lower()
            print(f"{role} role selected!!!")
            if role == 'exit':
                print('Exiting the system, GOODBYE!!!')
                sys.exit()
            if not self.validate_role(role):
                continue

            if role == 'librarian':
                choice = input("Do you want to (1)Register or (2)Login? ")

                if choice not in ['1','2']:
                    print("Invalid Selection!! Please select 1 or 2")
                    continue

                username = input("Enter Username: ")
                password = input("Enter Password: ")
                if choice == '1':
                    self.register_user(username,password,role='librarian')
                elif choice == '2':
                    if not self.login(username,password,role='librarian'):
                        continue
                else:
                    print("Invalid Selection!!!")
                print(self.logged_in_user)
                #print(self.logged_in_user.role)

                if self.logged_in_user and self.logged_in_user.role == 'librarian':
                    self.librarian_menu()

            elif role in ['faculty','student']:
                choice = input("Do you want to (1)Register or (2)Login? ")

                username = input("Enter Username: ")
                password = input("Enter Password: ")

                if choice == 1:
                    self.login(username,password,role=role)
                if choice ==1:
                    self.login(username,password,role=role)

            else:
                print("Invalid role selected. Please try again.")


    def librarian_menu(self):
        while True:
            print("\nWelcome to Librarian Menu")
            print("\nChoose what you want to do?\n1. Add Book\n2. Update Book\n3. Delete Book\n4. Search Book\n"
                  "5. Display All the Books\n6. Logout")
            choice = input("Enter your choice as number ")

            # Doing stuff based on the librarian choice
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.update_book()

            elif choice == '3':
                pass
            elif choice == '4':
                pass
            elif choice == '5':
                pass
            elif choice == '6':
                pass
            else:
                print("Invalid Choice!! Please Reselect!!!!")

    def student_menu(self):
        while True:
            print("Welcome to the student Menu\n")
            print("1. Search Book\n2. Display All the Books\n3. Logout")
            choice = input("Enter your choice as number ")

            # Doing stuff based on the student's choice
            if choice == '1':
                pass
            elif choice == '2':
                pass
            elif choice == '3':
                pass
            else:
                print("Invalid Choice!! Please Choose Again!!!")

    def faculty_menu(self):
        while True:
            print("Welcome to the Faculty Menu\n")
            print("1. Search Book\n2. Display All the Books\n3. Logout")
            choice = input("Enter your choice as number ")

            # Doing stuff based on the faculty's choice
            if choice == '1':
                pass
            elif choice == '2':
                pass
            elif choice == '3':
                pass
            else:
                print("Invalid Choice!! Please Choose Again!!!")


if __name__ == "__main__":
    library_system = LibraryManagementSystem()
    library_system.menu()

