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
'''
Данный лист нужен для преобразования общей удачливости студента в конкретную вероятность
(точнее, числитель данной вероятности) выпадения конкретного типа билета и экзаменатора
'''


class Student:
    luck = 0
    fatigue = {'easy': 0, 'middle': 0, 'hard': 0}
    knowledge = {'easy': 0, 'middle': 0, 'hard': 0}
    summary_knowledge = 0
    count_of_bot = 0

    def work_or_chill_decision(self, number_of_day):
        '''
        Эта функция реализует систему занятий с учётом усталости:
        - продуктивно заниматься можно лишь два раза в день - иначе штраф*
        (будет измененно)
        '''
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
        '''
        Данная функция учитывает влияние некой ситуации на общую удачливость студента
        '''
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
        '''
        Распределяет знания студента по билетам* (будет измененно позднее)
        '''
        self.knowledge['easy'] = min(self.summary_knowledge, 12)
        if self.summary_knowledge >= 12:
            self.summary_knowledge = self.summary_knowledge - 12
            self.knowledge['middle'] = min(self.summary_knowledge, 12)
        if self.summary_knowledge >= 12:
            self.summary_knowledge = self.summary_knowledge - 12

    def luck_result(self):
        '''
        Преобразует удачу студента в "язык вероятностей" (смотрите описание lucky_list)
        '''
        self.fatigue = lucky_list[self.luck + 3]

    def prepare_for_exam(self):
        '''
        Вызывает два служебных метода:
        - результат выборов студента (вероятность выпадения чего-либо) (luck_result)
        - распределение знаний студента по билетам* (будет измененно) (summary_preparation)
        '''
        self.luck_result()
        self.summary_preparation()
