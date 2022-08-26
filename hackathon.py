import json
from json.decoder import JSONDecodeError

from settings import DB
from datetime import datetime

list_ = """
[
    {
        "if": 1,
        "title": "macbook",
        "price": 1000
        "description": "macbook pro",
        "date_created": "24.08.22 19:05"
    },
    {
        "if": 2,
        "price": 1000
        "title": "Iphone",
        "descriptn": "Iphone 12 mini 256 gb",
        "date_created": "24.08.22 19:05"
    }
]
"""

def get_all_data():
    with open(DB) as f:
        try:
            return json.load(f)
        except JSONDecodeError:
            return []

# def get_price_data():
#     price = int(input('Введите сумму'))
#     obj_ = get_all_data()
#     for data in obj_:
#         if data['price'] > price:
#                 print(get_all_data())
#     with open(DB) as f:
#         json.load(f)

# get_price_data()




def create_data():
    id_ = datetime.now().strftime('%H%M%S')
    data = {
        'id': id_,
        'title': input('Введите название: '),
        'price': int(input('Введите цену: ')),
        'description': input('Введите описание: '),
        'data_created': datetime.now().strftime('%d.%m.%Y %H:%M'),
        'data_update': '',
        'status': 'Продается'

    }
    json_data: list = get_all_data()
    json_data.append(data)
    with open(DB, 'w') as f:
        json.dump(json_data, f, indent=4)


# def filter_():
#     id = input('Введите id: ')
# data = get_all_data()
# for i in data:
#     rek = {x for x in i if i['price'] < 20000}
#     print(rek)

def buy():
    id = input('Введите id: ')
    data = get_all_data()
    for i in data:
        if i['id'] == id:
            sum_ = int(input('Введите сумму: '))
            if i['price'] <= sum_:
                i['status'] = 'Продано'
            with open(DB, 'w') as f:
                json.dump(data, f, indent=4)
            return None
    for list in data:
        print('Такого id не существует!', '\n')
        print('id', list['id'], list['title'],'цена:', list['price'], '\n')
    buy()

# buy()



def get_data_by_id():
    id_ = input('Введите id: ')
    data = get_all_data()
    for obj in get_all_data():
        if obj['id'] == id_:
            return obj
        elif obj['id'] != id_:
            print('Такого id не существует!', '\n')
            for list in data:
                print('id', list['id'], list['title'], '\n')
            print(get_data_by_id())
            break


def delete_data():
    id_ = input('Введите id: ')
    data = get_all_data()
    for obj in data:
        if obj['id'] == id_:
            data.remove(obj)
            break
    with open(DB, 'w') as f:
        json.dump(data, f, indent=4)


    print('Такого id не существует!', '\n')
    for list in data:
        print('id', list['id'], list['title'], '\n')
    delete_data()
        


def update():
    id_ = input('Введите id: ')
    data = get_all_data()
    for obj in data:
        if obj['id'] == id_:
            obj['title'] = input('Введите название: ') or obj['title']
            try:
                obj['price'] = int(input('Введите цену: ')) or obj['price']
            except ValueError:
                obj['price']
            obj['description'] = input('Введите описание: ')     
            obj['data_update'] = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            with open(DB, 'w') as f:
                json.dump(data, f, indent=4)
            return None
    print('Такого id не существует!!!', '\n'
    'Выберите id нужного вам товара:', '\n'
            )
            
    for list in data:
        print('id', list['id'], list['title'], '\n')
    update()
         
def get_price():
    price_ = int(input('Введите цену: '))
    data = get_all_data()
    for obj in data:
        if obj['price'] > price_:
            print(obj)
    return 'Price is more than 100000'

def interface():
    info_data = """
        0. Список функций
        1. create - создать новый продукт
        2. delete - удалить продукт по id
        3. list - получить список всех продуктов
        4. retrieve - получить продукт по id
        5. update - изменить
        6. buy - купить товар
        7. exit - выйти из программы
        
        """  
    print(info_data)
    while True:
        name = input()
        if name == '0':
            print(info_data)
        elif name == '1':
            create_data()
        elif name == '2':
            delete_data()
        elif name == '3':
            print(get_all_data())
        elif name == '4':
            get_data_by_id()
        elif name == '5':
            update()
        elif name == '6':
            buy()
        elif name == '8':
            print(get_price())
        elif name == '7':
            break
        else:
            print('Функция с таким номером отсутствует')
            break

# data_ = get_all_data()

# for list in data_:
#     print('id', list['id'], list['title'])