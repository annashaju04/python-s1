class Publisher:
    def __init__(self, publisher):
        self.publisher = publisher


class Book(Publisher):
    def __init__(self, publisher, title, author):
        super().__init__(publisher)
        self.title = title
        self.author = author


class Python(Book):
    def __init__(self, publisher, title, author, price, pages):
        super().__init__(publisher, title, author)
        self.price = price
        self.pages = pages

    def display(self):
        print("Publisher Name:", self.publisher)
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Number of Pages:", self.pages)


# Main program
p = Python("Oxford", "Python Programming", "John", 450, 300)

p.display()
