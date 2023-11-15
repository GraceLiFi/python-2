# define your methods here.
# ex1() - ex10()
import dataclasses
from src.student.WordCounter import WordCounter
from src.student.TaxMan import TaxMan
from src.student.Calculator import Calculator
from src.student.CarCollector import CarCollector
from src.student.Fighter import Fighter
from src.student.Dwarf import Dwarf
from src.student.Invoice import Invoice
def ex1():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    sort_people(people_list, 'weight', 'desc')
    print(people_list)

def sort_people(people_list, feild, d):
    if d == 'desc':
        direction = True
    else:
        direction = False
    people_list.sort(key=lambda p: p[feild], reverse=direction)

def ex2():
    people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    filtered_list = filter_males(people_list)
    print(filtered_list)
    
def filter_males(people_list):
    new_list = list(filter(lambda p: p['sex'] == 'male', people_list))
    return new_list


def ex3():
    people_list = [
    {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
    {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
]
    new_people_list = calc_bmi(people_list)
    print(new_people_list)

def calc_bmi(person_list):
    def calc_person(p):
        weight = p['weight_kg']
        height = p['height_meters']
        bmi = round(weight / height ** 2, 1)
        return {**p, 'bmi': bmi}
    new_list = list(map(calc_person, person_list))
    return new_list

def ex4():
    people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]
    print(get_people(people_list))

def get_people(people_list):
    new_list = list((p['name'] for p in people_list if p['age'] >= 15))
    return new_list


def ex5():
    sentence = "This is a test of the emergency broadcast system"
    word_counter = WordCounter(sentence)
    word_counter.count_words()
    print(word_counter.get_word_count())
    print(word_counter.get_shortest_word())
    print(word_counter.get_longest_word())

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

def ex8():
    print(CarCollector.get_data())

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
    data = [
        "1, 2322, 10.00, False",
        "2, 5435, 60.30, True",
        "3, 3433, 15.63, False",
        "4, 8439, 12.77, False",
        "5, 3424, 11.34, False",
]
        
    print(Invoice.convert_data(data))