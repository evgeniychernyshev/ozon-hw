from app.lib import create_book, create_empty_book, add_book, search_books, search_book_by_id, remove_book_by_id, create_tags


container = list()
book_1 = dict()


def test_create_book_check_type():
    expected_type = 'class<dict>'
    actual = create_book('War and peace', 'Tolstoy', ['War', 'Love', 'Tolstoy'])
    assert str(type(actual)) == expected_type


def test_create_book_fields():
    expected_title = 'War and peace'
    expected_author = 'Tolstoy'
    expected_tags = ['War', 'Love', 'Tolstoy']
    actual = create_book('War and peace', 'Tolstoy', ['War', 'Love', 'Tolstoy'])
    global book_1
    book_1 = actual
    assert actual['title'] == expected_title and actual['author'] == expected_author and actual['tags'] == expected_tags


def test_create_empty_book():
    expected = {'id': 'new', 'title': '', 'author': '', 'tags': []}
    actual = create_empty_book()
    assert actual == expected


def test_add_book_check_type:
    expected_type = 'class<list>'
    actual = add_book(container, book_1)
    assert str(type(actual)) == expected_type


def test_search_books_by_title():
    pass


def test_search_books_by_author():
    pass


def test_search_books_by_tags():
    pass


def test_search_book_by_id():
    pass


def test_remove_book_by_id():
    pass


def test_create_tags():
    expected = ['War', 'Love', 'Tolstoy']
    actual = create_tags('War Love Tolstoy ')
    assert actual == expected
