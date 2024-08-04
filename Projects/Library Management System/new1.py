class Library:
    def __init__(self) -> None:
        self.number_of_books =  0
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        self.number_of_books = len(self.books)
        
    def show_info(self):
        print(f"The Library has {self.number_of_books} book(s) \n")

    def show_books(self):
        print(f"The Books are: ")
        for book in self.books:
            print(book)
        
l1 = Library()
l1.add_book("Harry Potter")
l1.add_book("Percy Jackson")
l1.add_book("Learn Python")

choice = int(input("Welcome the ABC Library \n (1) Check number of books in our Library \n (2) List of all our books \n Enter your choice: "))

if choice == 1:
    l1.show_info()
elif choice == 2:
    l1.show_books()
else:
    print("Enter a valid choice.")