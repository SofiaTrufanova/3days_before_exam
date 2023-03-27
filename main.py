import student_score
import result_functions

# В начале игры появляется студент - игрок
student = student_score.Student()

# Пока что это краткое описание 3-х дней студента
for day in range(1, 4):
    student.work_or_chill_decision(day)
    student.luck_decision(day * 2 - 1)
    student.work_or_chill_decision(day)
    student.luck_decision(day * 2)
    student.work_or_chill_decision(day)

# День перед экзаменом
student.prepare_for_exam()

# Студент тянет билет
ticket_type = result_functions.type_of_something(student.fatigue)
exam_type = result_functions.type_of_something(student.fatigue)

# Получаем результат экзамена
print('Ваша оценка:', result_functions.result(exam_type, ticket_type, student.knowledge))
