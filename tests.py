from main import BooksCollector
import pytest

@pytest.fixture
def collector():
    return BooksCollector()

def test_add_new_book_with_long_name(collector):
    collector.add_new_book('A' * 50)
    assert len(collector.get_books_genre()) == 0, "add_new_book не должен добавлять книгу с именем длиннее 40 символов"

def test_add_new_book_add_one_book(collector):

    collector.add_new_book("Book1")
    assert len(collector.get_books_genre()) == 1, "get_books_genre вернул одну книгу"

def test_set_book_genre_set_new_genre(collector):
    collector.add_new_book("Book1")
    collector.set_book_genre("Book1", "Фантастика")
    assert collector.get_book_genre("Book1") == "Фантастика", "set_book_genre установил жанр для книги"

def test_get_book_genre_non_existent_book(collector):
    assert collector.get_book_genre("NonExistentBook") is None, "get_book_genre вернул НЕ None для несуществующей книги"

def test_get_books_with_specific_genre_right_list_of_book(collector):
    collector.add_new_book("Book1")
    collector.add_new_book("Book2")
    collector.set_book_genre("Book1", "Фантастика")
    collector.set_book_genre("Book2", "Ужасы")
    books = collector.get_books_with_specific_genre("Фантастика")
    assert books == ["Book1"], "get_books_with_specific_genre вернул верный список книг"

def test_get_books_genre_right_list_of_genre(collector):
    collector.add_new_book("Book1")
    collector.add_new_book("Book2")
    collector.set_book_genre("Book1", "Фантастика")
    collector.set_book_genre("Book2", "Ужасы")
    books_genre = collector.get_books_genre()
    assert books_genre == {"Book1": "Фантастика", "Book2": "Ужасы"}, "get_books_genre вернул верный словарь жанров"

def test_get_books_for_children_right_list_of_book(collector):
    collector.add_new_book("Book1")
    collector.add_new_book("Book2")
    collector.set_book_genre("Book1", "Фантастика")
    collector.set_book_genre("Book2", "Комедии")
    children_books = collector.get_books_for_children()
    assert children_books != ["Book1"], "get_books_for_children вернул верный список книг"

def test_add_book_in_favorites(collector):
    collector.add_new_book("Book1")
    collector.add_book_in_favorites("Book1")
    assert "Book1" in collector.get_list_of_favorites_books(), "add_book_in_favorites добавил книгу в Избранное"

def test_delete_book_from_favorites(collector):
    collector.delete_book_from_favorites("Book1")
    assert "Book1" not in collector.get_list_of_favorites_books(), "delete_book_from_favorites удалил книгу из Избранного"

def test_get_list_of_favorites_books(collector):
    assert collector.get_list_of_favorites_books() == [], "get_list_of_favorites_books вернул список Избранных книг"

def test_add_book_in_favorites_invalid_book(collector):
    collector.add_book_in_favorites('NonExistentBook')
    assert len(collector.get_list_of_favorites_books()) == 0, "add_book_in_favorites не должен добавлять несуществующую книгу в избранное"
