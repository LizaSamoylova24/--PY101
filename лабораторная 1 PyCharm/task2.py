# TODO Найдите количество книг, которое можно разместить на дискете
disk_capacity_mb = 1.44
pages_in_book = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

disk_capacity_bytes = disk_capacity_mb * 1024 * 1024  # 1 Мб = 1024 * 1024 байт

size_of_book_bytes = pages_in_book * lines_per_page * chars_per_line * bytes_per_char


number_of_books = int( disk_capacity_bytes // size_of_book_bytes)


print("Количество книг, помещающихся на дискету:",number_of_books)
