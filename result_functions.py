import random


def type_of_something(fatigue):
    '''
    С заданной вероятностью выбираем один из трёх объектов
    '''
    easy = fatigue['easy']
    middle = fatigue['middle']
    r = random.randrange(1, 7)
    if r - easy < 0:
        return 'easy'
    if r - easy - middle < 0:
        return 'middle'
    return 'hard'


def result(type_of_exam, type_of_ticket, knowledge):
    '''
    Возвращаем результат экзамена в зависимости от удачи и знаний студента
    '''
    if type_of_exam == 'easy':
        return min(10, knowledge[type_of_ticket] + 2)
    if type_of_exam == 'middle':
        return min(10, knowledge[type_of_ticket])
    return min(10, knowledge[type_of_ticket] - 2)
