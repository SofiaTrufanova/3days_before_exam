import random

lucky_list = [{'easy': 0, 'middle': 3, 'hard': 3},
              {'easy': 1, 'middle': 2, 'hard': 3},
              {'easy': 1, 'middle': 3, 'hard': 2},
              {'easy': 2, 'middle': 2, 'hard': 2},
              {'easy': 2, 'middle': 3, 'hard': 1},
              {'easy': 3, 'middle': 2, 'hard': 1},
              {'easy': 4, 'middle': 1, 'hard': 1},
              {'easy': 4, 'middle': 2, 'hard': 0},
              {'easy': 5, 'middle': 1, 'hard': 0},
              {'easy': 6, 'middle': 0, 'hard': 0}]


class Student:
    luck = 0
    fatigue = {'easy': 0, 'middle': 0, 'hard': 0}
    knowledge = {'easy': 0, 'middle': 0, 'hard': 0}
    summary_knowledge = 0
    count_of_bot = 0

    def work_or_chill_decision(self, number_of_day):
        x = input('work or chill?\n')
        if x == 'work':
            self.count_of_bot += 1
            number_of_day += 1
            if self.count_of_bot > 2:
                self.summary_knowledge -= number_of_day * 2
                self.count_of_bot = 0
            else:
                self.summary_knowledge += 6

    def luck_decision(self, number_of_situation):
        x = input("first or second?\n")
        if number_of_situation == 1:
            if x == 'first':
                self.luck += 1
            else:
                self.luck -= 1
        if number_of_situation == 2:
            if x == 'second': self.luck += 1
        if number_of_situation == 3:
            if x == 'second': self.luck += 2
        if number_of_situation == 4:
            if x == 'first': self.luck -= 1
        if number_of_situation == 5:
            if x == 'second': self.luck -= 1
        if number_of_situation == 6:
            if x == 'first': self.luck += 2

    def summary_preparation(self):
        self.knowledge['easy'] = min(self.summary_knowledge, 12)
        if self.summary_knowledge >= 12:
            self.summary_knowledge = self.summary_knowledge - 12
            self.knowledge['middle'] = min(self.summary_knowledge, 12)
        if self.summary_knowledge >= 12:
            self.summary_knowledge = self.summary_knowledge - 12

    def luck_result(self):
        self.fatigue = lucky_list[self.luck + 3]

    def prepare_for_exam(self):
        self.luck_result()
        self.summary_preparation()


def type_of_something(fatigue):
    easy = fatigue['easy']
    middle = fatigue['middle']
    r = random.randrange(1, 7)
    if r - easy < 0:
        return 'easy'
    if r - easy - middle < 0:
        return 'middle'
    return 'hard'


def result(type_of_exam, type_of_ticket, knowledge):
    if type_of_exam == 'easy':
        return min(10, knowledge[type_of_ticket] + 2)
    if type_of_exam == 'middle':
        return min(10, knowledge[type_of_ticket])
    return min(10, knowledge[type_of_ticket] - 2)


student = Student()

for day in range(1, 4):
    student.work_or_chill_decision(day)
    student.luck_decision(day * 2 - 1)
    student.work_or_chill_decision(day)
    student.luck_decision(day * 2)
    student.work_or_chill_decision(day)

student.prepare_for_exam()

ticket_type = type_of_something(student.fatigue)
exam_type = type_of_something(student.fatigue)

print('Ваша оценка:', result(exam_type, ticket_type, student.knowledge))
