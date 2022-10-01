def menu() -> int:
    print('\nЧто делаем:\n'
          '1. Посмотреть весь справочник\n'
          '2. Поиск по фамилии\n'
          '3. Поиск по телефону\n'
          '4. Записать в справочник\n'
          '5. Сохранить справочник\n'
          '6. Закончить работу')
    choice = int(input())
    return choice

def directory_show(data, lst):
    for l in data:
        x = ''
        for v, k in l.items():
            x += f'{v}:{k}\n'
        print(x)


def directory_find_name() -> str:
    return input('Фамилия для поиска: ')


def directory_find_tel() -> str:
    return input('Телефон для поиска: ')


def directory_write() -> str:
    l_name = input('Фамилия: ')
    f_name = input('Имя: ')    
    tel_num = input('Номер телефона: ')
    comment = input('Коментарий: ')
    return f'{l_name}, {f_name}, {tel_num}, {comment} '

def preservation()->str:
    return input('Название файла: ')