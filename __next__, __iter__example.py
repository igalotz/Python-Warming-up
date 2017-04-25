import string


class Book(object):
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
        self.counter = 0

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter >= len(self.pages):
            raise StopIteration
        self.counter += 1
        return self.pages[self.counter - 1]


book = Book('Alphabet', list(string.ascii_uppercase))
print(book.title)
print(book.pages)

for page in book:
    print(page)


