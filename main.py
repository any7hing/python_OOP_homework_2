### first exersise

with open('food.txt', 'rt',encoding="utf-8") as file:
    cook_book = {}
    for line in file:
        food_name = line.strip()
        food_count = int(file.readline().strip())
        ingr = []
        for _ in range(food_count):
            ingridient_name,quantity,measure = file.readline().strip().split(' | ')
            ingr.append({
                'ingridient_name': ingridient_name, 
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[food_name] = ingr
# for key,value in cook_book.items(): # выводим красиво словарь с рецептами
#     print(key)
#     for i in cook_book[key]:
#         print(i)

###second exersise

def get_shop_list_by_dishes(dishes,person_count):
    ingr_list = {}
    buff = ""
    for dish in dishes: # создаем словарь ingr_list в котором будет финальный результат, и пробегаем по нему
        for value,some_dish in cook_book.items():
            if dish == value:
                for i in some_dish:
                    buff = i.pop('ingridient_name')
                    ingr_list[buff] = i
    
    for item,value in ingr_list.items(): # умножаем количество ингридиентов на количество персон
        value['quantity'] = int(value['quantity']) * int(person_count)

    for key,value in ingr_list.items(): # красиво выводим готовый словарь
        print(key,value)

# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

### third exersise

import os
current = os.getcwd()
result_list = {} # создаем словарь, где ключ - название файла, значение - содержимое файла

def read_file(file_name,folder_name='3exersise'): # считываем файл и записываем значение в словарь result_list
    current = os.getcwd()
    folder_name = folder_name
    file_name = file_name
    full_path = os.path.join(current, folder_name, file_name) 
    with open(full_path, encoding = "utf-8") as f:
        res = f.readlines()
        result_list[file_name] = res # ключем будет имя файла, а значением его содержимое

def whrite_file(result_list,folder='3exersise',final_result_name='final_result.txt'): # записываем значения в новый, итоговый файл(файл создается)
    current = os.getcwd()
    result_list = (sorted(result_list.items(), key=lambda item:len(item[1]))) # сортируем словарь result_list по длинне его значения(список с текстом) и сохраняем как список
    full_path = os.path.join(current, folder, final_result_name)
    with open(full_path, 'w') as f:
        for i in range(len(result_list)): # записываем в файл значения из списка result_list
            f.write(str(result_list[i][0]+ '\n')) # в 1 строку записываем название файла
            f.write(str(len(result_list[i][1]))+ '\n') # во 2 его длинну
            f.writelines(' '.join(result_list[i][1])+ '\n') # в 3 строку идет само содержимое файла

read_file("1.txt")
read_file("2.txt")
read_file("3.txt")
whrite_file(result_list)

    