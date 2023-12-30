class Library:
    def __init__(self):
        self.nobooks=0
        self.books=[]

    def addbook(self,book):
        self.books.append(book)
        self.nobooks=len(self.books)

    def showinfo(self):
        print(f"The Library has {self.nobooks} books The Books are:")
        for book in self.books:
            print(book)


L1=Library()
L1.addbook("The Alchemist",)
L1.addbook("Think Straight",)
L1.addbook("You Only Live Once",)
L1.addbook("Revolution 2020",)
L1.addbook("Theory Of Everything",)
L1.addbook("Believe in Yourself",)
L1.addbook("You Can",)
L1.addbook("Do It Today",)
L1.addbook("Be Your Own Sunshine",)
L1.addbook("Where The Sun Never Sets",)
L1.showinfo()





