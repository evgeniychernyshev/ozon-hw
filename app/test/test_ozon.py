from app.lib import create_book, create_empty_book, add_book, search_books, search_book_by_id, remove_book_by_id, create_tags


container = list()
book_1 = dict()
book_2 = dict()
book_3 = dict()


def test_create_book():
    expected_title = 'War and peace'
    expected_author = 'Tolstoy'
    expected_tags = ['War', 'Love', 'Tolstoy']
    global book_1, book_2, book_3
    book_1 = create_book('War and peace', 'Tolstoy', ['War', 'Love', 'Tolstoy'])
    book_2 = create_book('Anna Karenina', 'Tolstoy', ['Train', 'Love', 'Tolstoy'])
    book_3 = create_book('Mu-mu', 'Turgenev', ['Slave', 'Dog', 'Turgenev'])
    actual = book_1

    assert actual['title'] == expected_title and actual['author'] == expected_author and actual['tags'] == expected_tags


def test_add_book():
    expected = list()
    expected.append(book_1)
    global container
    container = add_book(container, book_1)
    actual = container
    container = add_book(container, book_2)
    container = add_book(container, book_3)

    assert actual == expected


def test_create_empty_book():
    expected = {'id': 'new', 'title': '', 'author': '', 'tags': []}
    actual = create_empty_book()

    assert actual == expected


def test_search_books_by_title():
    expected = list()
    expected.append(book_2)
    actual = search_books(container, 'Anna')

    assert actual == expected


def test_search_books_by_author():
    expected = list()
    expected.append(book_3)
    actual = search_books(container, 'Turgenev')

    assert actual == expected


def test_search_books_by_tags():
    expected = list()
    expected.append(book_1)
    actual = search_books(container, '#War')

    assert actual == expected


def test_search_book_by_id():
    id = book_1['id']
    expected = book_1
    actual = search_book_by_id(container, id)

    assert actual == expected


def test_remove_book_by_id():
    id = book_2['id']
    expected = list()
    expected.append(book_1)
    expected.append(book_3)
    actual = remove_book_by_id(container, id)

    assert actual == expected


def test_create_tags():
    expected = ['War', 'Love', 'Tolstoy']
    actual = create_tags('War Love Tolstoy ')

    assert actual == expected
