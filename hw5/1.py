"""
1.	Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""
# ВАРИАНТ 1
user_file = open('user_file.txt', 'w')
user_file.close()
with open('user_file.txt', 'a') as uf:
    while True:
        text_to_wr = input('Введите данные: ')
        if text_to_wr == '':
            break
        uf.write(f'\n {text_to_wr}')
uf = open('user_file.txt', 'r')
print('Записи фала после вынесения данных: ', uf.read())
uf.close()

# ВАРИАНТ 2
# list_data_to_uf = []
# while True:
#     text_to_wr = input('Введите данные: ')
#     if text_to_wr == '':
#         break
#     else:
#         list_data_to_uf.append(text_to_wr)
# with open('user_file.txt', 'w') as uf:
#     for line in list_data_to_uf:
#         uf.write(f'\n {line}')
# uf = open('user_file.txt', 'r')
# print('Записи фала после вынесения данных: ', uf.read())
# uf.close()