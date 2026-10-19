class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)


class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.__number_of_pages = 0
        self.set_number_of_pages(number_of_pages)

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, pages):
        if pages > 0:
            self.__number_of_pages = pages
        else:
            print("The number of pages must be positive")

    def display_info(self):
        super().display_info()
        print("Number of pages:", self.__number_of_pages)


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = 0
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, number):
        if number > 0:
            self.__issue_number = number
        else:
            print("The issue number must be positive")

    def display_info(self):
        super().display_info()
        print("Issue number:", self.__issue_number)


pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
pub2 = Publication("Encyclopedia of Science", "Various Authors")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("The Great Gatsby", "F.Scott Fitzgerald", 180)
mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("Time", "Various Authors", 15)

for item in [pub1, pub2, book1, book2, mag1, mag2]:
    item.display_info()
    print()

Book("Test Book", "Test Author", -5)         
Magazine("Test Magazine", "Test Author", 0)
