"""Задача №49. Решение в группах
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной

Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных.
"""

def check_number(tel_number):
    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f:
            if tel_number in line:
                return True
        return False

def write(text):
    with open("data.txt", "a", encoding="utf-8") as f:
        f.writelines(text)
        f.writelines("\n")
        print("Успешно")


def read_all():
    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line[:-1])


def get_by_name(name):
    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f:
            if name in line:
                print(line)

def change_data(words):
    f = open ('data.txt', 'r', encoding="utf-8")
    old_data = f.read()
    new_data = old_data.replace(words, input("Введите новые данные: "))
    with open ('data.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)

def remove_data(words):
    f = open ('data.txt', 'r', encoding="utf-8")
    old_data = f.read()
    new_data = old_data.replace(words, "")
    with open ('data.txt', 'w', encoding="utf-8") as f:
        f.write(new_data)
        print("Данные удалены")

def choose(choice):
        if choice == '1': write(input("Введите ваши данные, например:(Фамилия Имя Отчество Телефон) "))
        if choice == "2": read_all()
        if choice == "3": get_by_name(input("Введите имя, фамилию, отчество "))
        if choice == "4": change_data(input('Введите данные, которые хотите заменить '))
        if choice == "5": remove_data(input('Введите данные, которые хотите удалить '))
        if choice == "6": exit()

def print_main():
    return print('Выберите действие: \n 1 - Запись данных в файл \n 2 - Печать всех данных \n '
                 '3 - Поиск по данным \n 4 - Замена данных \n '
                 '5 - Удаление данных \n 6 - Выход \n')

print_main()
choose(input("Введите номер команды из меню: "))
