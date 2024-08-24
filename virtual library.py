class Library:
      def __init__(self,listofbooks):
            self.availablebooks=listofbooks

      def displayAvailablebooks(self):
                   print("The books we have in our library are as follows:")
                   for book in self.availablebooks:
                         print(book)
      def lendBook(self,requestedBook):
            if requestedBook in self.availablebooks:
                  print("The book you requested has now been borrowed")
            else:
                  print("Sorry the book you have requested is currently not in the library")
                  
      def addBook(self,returnedBook):
            print("Thanks for returning your borrowed book")
            

class Student:
      def requestBook(self):
            print("Enter the name of the book you'd like to borrow:")
            self.book=input()
            return self.book

      def returnBook(self):
            print("Enter the name of the book you'd like to return:")
            self.book=input()
            return self.book

def main():            
      library=Library(["The Last Battle","The Screwtape letters","The Great Divorce","Think python"])
      student=Student()
      done=True
      while done==True:
            print("""\t\t\tLIBRARY MENU\t\t\t
                  1. Display all available books
                  2. Request a book
                  3. Return a book
                  4. Exit
                  """)
            choice=int(input("Enter Choice:"))
            if choice==1:
                        library.displayAvailablebooks()
            elif choice==2:
                        print("Enter your name:")
                        name=input()
                        library.lendBook(student.requestBook())
                        break
            elif choice==3:
                        print("Enter your name:")
                        name=input()
                        library.addBook(student.returnBook())
                        break
            elif choice==4:
                  sys.exit()
                  
main()
