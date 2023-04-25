import globals
import result_functions


class Student:
    """Студент (игрок)"""

    def __init__(self):
        self.luck = 0
        self.fatigue = {'easy': 0, 'middle': 0, 'hard': 0}
        self.knowledge = {'easy': 0, 'middle': 0, 'hard': 0}
        self.summary_knowledge = 0
        self.overworking = 0
        self.count_of_bot = 0
        self.result = 0

    def is_student_lucky(self):
        if result_functions.one_half():
            self.luck += 1
            return True
        return False

    def work_or_chill_decision(self, choice, index):
        """
        Эта функция реализует систему занятий с учётом усталости:
        - продуктивно заниматься можно лишь два раза в день - иначе штраф.
        При этом возращается 0, если студент не занимался, 1 - если позанимался хорошо
        и 2 - если он переутомился
        """
        work = 0
        if index % 3 == 0:
            self.count_of_bot = 0
        if choice == 'first':
            self.count_of_bot += 1
            if self.count_of_bot > 2:
                self.overworking += 1
                self.count_of_bot = 0
                work = 2
            else:
                self.summary_knowledge += 1
                work = 1
        return work

    def luck_decision(self, number_of_situation, choice):
        """ Данная функция учитывает влияние некой ситуации на общую удачливость студента.
        Возвращает True, если студенту повезло, иначе - False. """
        if number_of_situation != 2 and number_of_situation != 6:  # рандом
            return self.is_student_lucky()
        is_it_luck = True
        if number_of_situation == 2:  # детерминированная удача (1 выбор лучше)
            if choice == 'first':
                self.luck += 1
            else:
                self.luck -= 1
                is_it_luck = False
        if number_of_situation == 6:  # детерминированная удача (1 выбор лучше)
            if choice == 'first':
                self.luck += 2
            else:
                is_it_luck = False
        return is_it_luck

    def penalty(self):
        """
        Добавляет штраф
        """
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
        """
        Распределяет знания студента по билетам и добавляет штраф
        """
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
        """
        Преобразует удачу студента в "язык вероятностей" (смотрите описание lucky_list)
        """
        self.fatigue = globals.Global.lucky_list[self.luck + 3]

    def prepare_for_exam(self):
        """
        Вызывает два служебных метода:
        - результат выборов студента (вероятность выпадения чего-либо) (luck_result)
        - распределение знаний студента по билетам* (будет измененно) (summary_preparation)
        """
        self.luck_result()
        self.summary_preparation()
