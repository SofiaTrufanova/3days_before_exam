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
    '''
    Студент (игрок)
    '''
    luck = 0
    fatigue = {'easy': 0, 'middle': 0, 'hard': 0}
    knowledge = {'easy': 0, 'middle': 0, 'hard': 0}
    summary_knowledge = 0
    overworking = 0
    count_of_bot = 0

    def work_or_chill_decision(self):
        '''
        Эта функция реализует систему занятий с учётом усталости:
        - продуктивно заниматься можно лишь два раза в день - иначе штраф*
        (будет измененно)
        '''
        x = input('work or chill?\n')
        if x == 'work':
            self.count_of_bot += 1
            if self.count_of_bot > 2:
                self.overworking += 1
                self.count_of_bot = 0
            else:
                self.summary_knowledge += 1

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

    def penalty(self):
        '''
        Добавляет штраф
        '''
        if self.overworking < self.knowledge['hard']:
            self.knowledge['hard'] -= self.overworking
            if self.overworking < self.knowledge['middle']:
                self.knowledge['middle'] -= self.overworking
            else:
                self.knowledge['easy'] = max(0, self.knowledge['easy'] - self.overworking + self.knowledge['middle'])
                self.knowledge['middle'] = 0
        else:
            new_overworking = self.overworking - self.knowledge['hard']
            self.knowledge['hard'] = 0
            if self.overworking + new_overworking < self.knowledge['middle']:
                self.knowledge['middle'] -= self.overworking + new_overworking
            else:
                self.knowledge['easy'] = max(0, self.knowledge['easy'] - self.overworking + self.knowledge[
                    'middle'] - new_overworking)
                self.knowledge['middle'] = 0

    def summary_preparation(self):
        '''
        Распределяет знания студента по билетам и добавляет штраф
        '''
        self.knowledge['easy'] = min(12, self.summary_knowledge * 3)
        if self.summary_knowledge <= 4:
            self.knowledge['middle'] = self.summary_knowledge * 2
        else:
            self.knowledge['middle'] = 12
        if self.summary_knowledge <= 4:
            self.knowledge['hard'] = self.summary_knowledge
        elif self.summary_knowledge == 5:
            self.knowledge['hard'] = 6
        else:
            self.knowledge['hard'] = 12
        self.penalty()

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