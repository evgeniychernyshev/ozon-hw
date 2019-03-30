from app.lib import create_book, add_book, list_books, search_books

# TODO: tags - новый ключ в dict'е
# TODO: tags - война, любовь, толстой
# TODO: tags - поезд, любовь, толстой
# TODO: 1. Как хранить (тип данных)
# TODO: 2. Как искать (полное совпадение???)
# TODO: 3. Написать функция поиска по тегам
# TODO (advanced): искать по тегам #имя_тега (той же функцией search_books)

books = []

war_and_piece = create_book(
    'Война и мир',
    'Толстой',
    1000,
    True
)

anna_karenina = create_book(
    'Анна Каренина',
    'Толстой',
    500,
    False
)

# print(list(anna_karenina.keys()))

# alt + enter - что-то пофиксить, alt + insert - что-то создать
add_book(books, war_and_piece)
add_book(books, anna_karenina)

print(books)

print(list_books(books, 1, 1))
print(list_books(books, 2, 1))


# print(list_books(books, 10, 1))

print(search_books(books, 'каре'))
print(search_books(books, 'толстой'))
print(search_books(books, 'стругацкие'))