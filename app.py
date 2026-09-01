# OBS-02: Display books
# OBS-03: Search books

books = [
    {"id": 1, "title": "Python Basics", "author": "John Smith", "price": 400},
    {"id": 2, "title": "Data Structures", "author": "Mark Allen", "price": 450},
    {"id": 3, "title": "Machine Learning", "author": "Andrew Ng", "price": 700},
    {"id": 4, "title": "Web Development", "author": "Robert Martin", "price": 600}
]


def display_books():
    """Display all available books."""
    return books


def search_books(keyword):
    """Search books by title or author."""
    keyword = keyword.lower()

    return [
        book for book in books
        if keyword in book["title"].lower()
        or keyword in book["author"].lower()
    ]


def add_book(title, author, price):
    """OBS-04: Add a new book."""
    new_book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "price": price
    }

    books.append(new_book)
    return new_book


if __name__ == "__main__":

    print("================================")
    print("       ONLINE BOOK STORE")
    print("================================")

    print("\nAvailable Books:")

    for book in display_books():
        print(
            f"{book['id']}. {book['title']} - "
            f"{book['author']} - ₹{book['price']}"
        )

    keyword = input("\nEnter book title/author to search: ")

    results = search_books(keyword)

    print("\nSearch Results:")

    if results:
        for book in results:
            print(
                f"{book['title']} - "
                f"{book['author']} - ₹{book['price']}"
            )
    else:
        print("No books found.")
