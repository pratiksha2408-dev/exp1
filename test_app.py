from app import display_books, search_books, add_book


def test_display_books():
    books = display_books()

    assert len(books) > 0


def test_search_books():
    results = search_books("Python")

    assert len(results) > 0
    assert results[0]["title"] == "Python Basics"


def test_search_by_author():
    results = search_books("Andrew")

    assert len(results) > 0
    assert results[0]["author"] == "Andrew Ng"


def test_invalid_search():
    results = search_books("XYZ123")

    assert len(results) == 0


def test_add_book():
    old_count = len(display_books())

    add_book("AI Fundamentals", "David Kumar", 500)

    assert len(display_books()) == old_count + 1
