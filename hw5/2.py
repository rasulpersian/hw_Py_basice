"""
2.Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт
строк и слов в каждой строке.
"""
import os
try:
    with open('file_to_2lesson.txt', 'w+', encoding='utf-8') as file_to_2lesson:
        text_to_save = 'Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт ' \
                       'строк и слов в каждой строке.'
        list_of_text = text_to_save.split(',')
        for line in list_of_text:
            file_to_2lesson.write(f'\n{line}')
        print(f' Содержимое файла после записи: {list_of_text}')
    file = open('file_to_2lesson.txt', 'r', encoding='utf-8')
    content = file.readlines()
    print(f' Кол. строк файле: {len(file.readlines())}')
    for n in range(len(content)):
        print(f'Количество слов в строке {n} = {len(content[n].split())}')
    file.close()
    # rm_file = input('Удалить файл?(y/n): ')
    # if rm_file == 'y':
    #     os.remove('file_to_2lesson.txt')

except IOError:
    print('Произошла ошибка ввода-вывода')


