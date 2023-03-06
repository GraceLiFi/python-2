from students.stu0.TaxMan import TaxMan
from students.stu0.Calculator import Calculator
from students.stu0.WordCounter import WordCounter
from students.stu0.CarCollector import CarCollector
from students.stu0.Dwarf import Dwarf
from students.stu0.Fighter import Fighter
from students.stu0.Character import Character
from pprint import pprint

def ex1():
    people_list = [
        {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
        {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    sort_people(people_list, 'weight', 'desc')
    pprint(people_list)


def ex2():
    people_list = [
        {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
        {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    filtered_list = filter_people(people_list)
    pprint(filtered_list)


def ex3():
    people_list = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]
    new_people_list = calc_bmi(people_list)
    pprint(new_people_list)


def ex4():
    people_list = [
        {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
        {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    pprint(get_people(people_list))


def ex5():
    pprint(CarCollector.get_data())


def ex6():
    items = [
        {"id": 1, "desc": "clock", "price": 1.00},
        {"id": 2, "desc": "socks", "price": 2.00},
        {"id": 3, "desc": "razor", "price": 3.00},
    ]
    tm = TaxMan(items, "10%")
    tm.calc_total()
    print(tm.get_total())


def ex7():
    sentence = "This is a test of the emergency broadcast system"
    word_counter = WordCounter(sentence)
    word_counter.count_words()
    print(word_counter.get_word_count())
    print(word_counter.get_shortest_word())
    print(word_counter.get_longest_word())


def ex8():
    calculator1 = Calculator(4, 3)
    calculator1.add()
    print(calculator1.get_result())

    calculator2 = Calculator(4, 3)
    calculator2.sub()
    print(calculator2.get_result())

    calculator3 = Calculator(2, 3)
    calculator3.mul()
    print(calculator3.get_result())

    calculator4 = Calculator(8, 2)
    calculator4.div()
    print(calculator4.get_result())


def ex9():
    f = Fighter(18)
    d = Dwarf(15)
    print(f)
    print(d)
    f.fight(d)
    d.fight(f)
    print(f)
    print(d)



def ex10():
    pass


#
# Place your functions here...
#


def sort_people(people, field, direction):
    people.sort(key=lambda p: p[field], reverse=False if direction == "asc" else True)


def filter_people(people):
    return list(filter(lambda p: p['sex'] == 'male', people))


def calc_bmi(people):
    return list(map(lambda p:
                    {
                        'id': p['id'],
                        'name': p['name'],
                        'weight_kg': p['weight_kg'],
                        'height_meters': p['height_meters'],
                        'bmi': round(p['weight_kg'] / p['height_meters'] ** 2, 1)
                    },
                    people))


def get_people(people):
    return [p['name'] for p in people if p['age'] >= 15]

def combine(car_list, car_dict):
    # print(car_list)
    # print(car_dict)

    mm = list(map(transform, car_list))
    print(mm)
    return car_list


def transform(m):
    retval = {
        "id": 1,
        "make": 'toybota',
        "price": 1.00
    }
    return retval
