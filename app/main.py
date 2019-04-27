from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect
from app.lib import create_book, add_book, search_books, search_book_by_id, remove_book_by_id, create_empty_book, create_tags


def main():
    app = Flask(__name__)

    container = []
    wp = create_book('War and peace', 'Tolstoy', ['War', 'Love', 'Tolstoy'])
    anna = create_book('Anna Karenina', 'Tolstoy', ['Train', 'Love', 'Tolstoy'])

    #TODO: сделать распаковку в add_book
    container = add_book(container, wp)
    container = add_book(container, anna)

    @app.route('/')
    def index():
        search = request.args.get('search')
        if search:
            # TODO: почистить
            results = search_books(container, search)
            return render_template('index.html', books=results, search=search)

        return render_template("index.html", books=container)

    @app.route('/books/<book_id>')
    def book_details(book_id):
        result = search_book_by_id(container, book_id)
        return render_template('book-details.html', book=result)

    @app.route('/books/<book_id>/edit')
    def book_edit(book_id):
        book = None
        if book_id == 'new':
            book = create_empty_book()
        else:
            book = search_book_by_id(container, book_id)
        return render_template('book-edit.html', book=book)

    @app.route('/books/<book_id>/save', methods=['POST'])
    def book_save(book_id):
        nonlocal container
        title = request.form['title']
        author = request.form['author']
        tags = create_tags(request.form['tags'])
        if book_id == 'new':
            book = create_book(title=title, author=author, tags=tags)
            container = add_book(container, book)
        else:
            book = search_book_by_id(container, book_id)
            book['title'] = request.form['title']
            book['author'] = request.form['author']
            book['tags'] = create_tags(request.form['tags'])
        return redirect(url_for('book_details', book_id=book['id']))

    @app.route('/books/<book_id>/remove', methods=['POST'])
    def book_remove(book_id):
        nonlocal container
        container = remove_book_by_id(container, book_id)
        return redirect(url_for('index'))

    app.run(port=9877, debug=True)


if __name__ == '__main__':
    main()


# from app.lib import create_book, add_book, list_books, search_books
#
# books = []
#
# war_and_piece = create_book(
#     'Война и мир',
#     'Толстой',
#     1000,
#     True,
#     ['Война', 'Любовь', 'Толстой']
# )
#
# anna_karenina = create_book(
#     'Анна Каренина',
#     'Толстой',
#     500,
#     False,
#     ['Поезд', 'Любовь', 'Толстой']
# )
#
# # print(list(anna_karenina.keys()))
#
# # alt + enter - что-то пофиксить, alt + insert - что-то создать
# add_book(books, war_and_piece)
# add_book(books, anna_karenina)
#
# # print(books)
# # print(list_books(books, 1, 1))
# # print(list_books(books, 2, 1))
# # print(list_books(books, 10, 1))
#
# print(search_books(books, 'каре'))
# print(search_books(books, 'толстой'))
# print(search_books(books, 'стругацкие'))
# print(search_books(books, '#поезд'))
# print(search_books(books, '#во'))