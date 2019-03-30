from app.lib import create_book, add_book, list_books, search_books

books = []

war_and_piece = create_book(
    'Война и мир',
    'Толстой',
    1000,
    True,
    ('Война', 'Любовь', 'Толстой')
)

anna_karenina = create_book(
    'Анна Каренина',
    'Толстой',
    500,
    False,
    ('Поезд', 'Любовь', 'Толстой')
)

# print(list(anna_karenina.keys()))

# alt + enter - что-то пофиксить, alt + insert - что-то создать
add_book(books, war_and_piece)
add_book(books, anna_karenina)

# print(books)
# print(list_books(books, 1, 1))
# print(list_books(books, 2, 1))
# print(list_books(books, 10, 1))

print(search_books(books, 'каре'))
print(search_books(books, 'толстой'))
print(search_books(books, 'стругацкие'))
print(search_books(books, '#поезд'))
print(search_books(books, '#во'))