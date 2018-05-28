cook_book = {} # Задаем глобальную переменную - пустой словарь рецептов


def get_cook_book():
    with open('cook_book.txt') as f:
        while True:
            dish_name = f.readline().lower().strip()  # Получили ключ словара - название блюда в нижнем регистре
            if not dish_name:
              break
            number_of_cycles = int(f.readline().strip())  # Получили кол-во строк для считывания ингредиентов в блюде

            ingredients_list = []  # Задали пустой словарь, куда будем складывать словари ingredient_dict
            while number_of_cycles:
                ingredient_dict = {}
                ingred_list = f.readline().strip().split(' | ')  # Получили список типа ['Яйцо', '2', 'шт;]
                ingredient_dict['ingridient_name'] = ingred_list[0]
                ingredient_dict['quantity'] = int(ingred_list[1])
                ingredient_dict['measure'] = ingred_list[2]
                ingredients_list = ingredients_list + [ingredient_dict]  # Добавили словарь ingredient_dict с список ingredients_list
                number_of_cycles -= 1
            f.readline() #  Сделали проход пустой строки
            cook_book[dish_name] = ingredients_list # сформировали словарь cook_book по конкретному dish_name
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = get_cook_book()
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'],
                                                      shop_list_item['quantity'], shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print('Список продуктов для приготовления заказа:')
    print_shop_list(shop_list)


create_shop_list()