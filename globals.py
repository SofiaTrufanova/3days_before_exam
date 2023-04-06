import student_score

class Global():
    'Глобальные переменные программы, а также константы'
    student = student_score.Student()
    click_index = 0
    lucky_index = 0
    study_index = 0
    day = 0
    no_power = 0
    is_luck = False
    ticket_type = 0
    exam_type = 0
    lucky_list = [{'easy': 0, 'middle': 2, 'hard': 4},
                  {'easy': 0, 'middle': 3, 'hard': 3},
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
