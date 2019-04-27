import uuid


def create_book(title, author, tags):
    return {
        'id': str(uuid.uuid4()),
        'title': title,
        'author': author,
        'tags': tags
    }


def create_empty_book():
    return {
        'id': 'new',
        'title': '',
        'author': '',
        'tags': []
    }


def add_book(container, book):
    copy = container[:]
    copy.append(book)
    return copy


def search_books(container, search):  # search - строка поиска
    search_lowercased = search.strip().lower()  # 1. search.strip() 2. (результат search.strip()).lower()
    result = []
    for book in container:
        if search_lowercased in book['title'].lower():
            result.append(book)
            continue

        if search_lowercased in book['author'].lower():
            result.append(book)
            continue

        for tag in book['tags']:
            if tag.lower() == search_lowercased.strip('#'):
                result.append(book)
                continue
    return result


def search_book_by_id(container, id):
    for book in container:
        if book['id'] == id:
            return book


def remove_book_by_id(container, book_id):
    result = []
    for book in container:
        if book['id'] != book_id:
            result.append(book)
    return result


def create_tags(tags):
    tags = tags.strip(' ')
    return tags.split(' ')
