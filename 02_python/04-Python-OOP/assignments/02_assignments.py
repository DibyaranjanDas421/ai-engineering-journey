class Book:

    def __init__(self,title,author,reviews=None):
        self.title=title
        self.author=author
        
        if reviews is None:
            self.reviews=[]
        else:
            self.reviews=reviews


book1=Book("Pyython","Jhon")
book1.reviews.append("Very good!")

print(book1.reviews)
