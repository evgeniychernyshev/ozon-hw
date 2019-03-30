def create_book(title, author, price, availability):
    return {
        'title': title,
        'author': author,
        'price': price,
        'available': availability
    }


def add_book(container, book):  # не чистая функция
    container.append(book)
    # return container # TODO: вернуться к этому вопросу позже


def list_books(container, page, page_size):
    # page_size = 50
    start = (page - 1) * page_size  # для первой страницы стартуем с 0
    finish = start + page_size
    return container[start:finish]


def search_books(container, search):  # search - строка поиска
    search_lowercased = search.strip().lower()  # 1. search.strip() 2. (результат search.strip()).lower()
    result = []
    for book in container:
        if search_lowercased in book['title'].lower():
            result.append(book)
            continue  # не даёт идти дальше на 30 строку

        if search_lowercased in book['author'].lower():
            result.append(book)
            continue  # пока не нужно, но на будущее пригодиться, если будем добавлять новые возможности

    return result
