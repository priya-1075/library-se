class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise ValueError("Duplicate Book ID")
        self.books[book_id] = {
            "title": title,
            "author": author,
            "status": "Available"
        }

    def borrow_book(self, book_id):
        if self.books[book_id]["status"] == "Borrowed":
            raise ValueError("Book already borrowed")
        self.books[book_id]["status"] = "Borrowed"

    def return_book(self, book_id):
        self.books[book_id]["status"] = "Available"

    def generate_report(self):
        report = "Book ID | Title | Author | Status\n"
        for bid, b in self.books.items():
            report += f"{bid} | {b['title']} | {b['author']} | {b['status']}\n"
        return report

