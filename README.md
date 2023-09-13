# qa_python

test_add_new_book_with_long_name - добавление книги где длина названия больше 40 символов
Проверка: вызываем метод get_books_genre и считаем количество элементов

test_add_new_book_add_one_book - добавление одной новой книги
Проверка: вызываем get_books_genre и считаем количество элементов

test_set_book_genre_set_new_genre - устанавливаем книге жанр
Проверка: вызываем get_book_genre и проверяем что жанр установлен

test_set_book_genre_with_invalid_genre - устанавливаем не существующий жанр
Проверка: вызываем get_book_genre и проверяем что жанр не установился

test_get_book_genre_non_existent_book
Проверка: вызываем get_book_genre пустой для несуществующей книги

test_get_books_with_specific_genre_right_list_of_book - добаляем 2 книги и жанры для книг
Проверка: сверяем что книга 1 в списке определенных жанров

test_get_books_genre_right_list_of_genre - добаляем 2 книги и жанры для книг
Проверка: сверяем что вернулся верный словарь жанров

test_get_books_for_children_right_list_of_book - добаляем 2 книги и жанры для книг
Проверка: сверяем что вернулся верный список книг

test_add_book_in_favorites - добаляем книгу в избраное
Проверка: книга есть в списке избранного

test_delete_book_from_favorites - удаляем книгу с избранного
Проверка: список книг пустой

test_add_book_in_favorites_invalid_book - доюалвяем  в избранное несуществующую книгу
Проверка: вызываем метод get_list_of_favorites_books и считаем количество элементов




