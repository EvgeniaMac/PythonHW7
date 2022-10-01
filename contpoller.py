from view import (directory_find_name, directory_find_tel, menu,
                  directory_show, directory_write, preservation)
from mod import (write_csv, write_txt, read_scv, add_user,
                 find_name, find_tel)


def work_phbook():
    ch = menu()
    ph_book = read_scv('PHBook.csv')
    while ch != 6:
        if ch == 1:
            menu(ph_book)
        elif ch == 2:
            name = directory_find_name()
            print(directory_find_name(ph_book, name))
        elif ch == 3:
            num = directory_find_tel()
            print(directory_find_tel(ph_book, num))
        elif ch == 4:
            user_data = directory_write()
            add_user(ph_book, user_data)
            write_csv('PHBook.csv', ph_book)
        elif ch == 5:
            file_name = preservation()
            write_csv(file_name, ph_book)
        ch = menu()
