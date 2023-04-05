from tkinter import *
import text
import student_score
import result_functions

click_index = 0
lucky_index = 0
study_index = 0
day = 0
no_power = 0
is_luck = False
ticket_type = 0
exam_type = 0

student = student_score.Student()


def final(event):
    global click_index, ticket_type, exam_type
    label_text.configure(text=text.key_situations[-1])
    if click_index == 16:
        if ticket_type == 'easy':
            main_text.configure(text='Вы тянете лёгкий билет!')
        elif ticket_type == 'middle':
            main_text.configure(text='Вы тянете обычный билет.')
        else:
            main_text.configure(text='Вы тянете сложный билет... Это формула Грина.')
    if click_index == 17:
        if exam_type == 'easy':
            main_text.configure(
                text='Вы сели его расписывать, и тут экзаменатор называет ваше имя. Вы оборачиваетесь и смотрите на экзаменатора:'
                     ' он выглядит добрым)')
        elif exam_type == 'middle':
            main_text.configure(
                text='Вы сели его расписывать, и тут экзаменатор называет ваше имя. Вы оборачиваетесь и смотрите на экзаменатора:'
                     'он выглядит как среднестатистический экзаменатор.')
        else:
            main_text.configure(
                text='Вы сели его расписывать, и тут экзаменатор называет ваше имя. Вы оборачиваетесь и смотрите на экзаменатора:'
                     ' это Иванова...')
    if click_index == 18:
        main_text.configure(
            text='В итоге Вы рассказываете свой билет экзаменатору. Он задаёт вам вопросы и в итоге отпускает вас...')
    click_index += 1
    if click_index == 19:
        final_result = max(2, min(student.result, 10))
        label_text.configure(text=text.result_text[final_result - 2])
        main_text.grid_remove()
        window.bind("<Button-1>", do_nothing)


def do_nothing(event):
    pass


def next_click(event):
    global click_index, lucky_index, study_index, day, ticket_type, exam_type
    window.bind("<Button-1>", do_nothing)
    main_text.configure(text=text.main_text[click_index])
    click_index += 1
    if click_index >= 16:
        first_study_button.grid_remove()
        second_study_button.grid_remove()
        first_lucky_button.grid_remove()
        second_lucky_button.grid_remove()
        student.prepare_for_exam()
        ticket_type = result_functions.type_of_something(student.fatigue)
        exam_type = result_functions.type_of_something(student.fatigue)
        student.result = result_functions.result(exam_type, ticket_type, student.knowledge)
        window.bind("<Button-1>", final)
    else:
        if is_luck:
            first_study_button.grid(column=0, row=4)
            second_study_button.grid(column=4, row=4)
        elif study_index % 3 == 0:
            label_text.configure(text=text.key_situations[day])
            day += 1
            first_study_button.grid(column=0, row=4)
            second_study_button.grid(column=4, row=4)
        else:
            first_lucky_button.grid(column=0, row=4)
            second_lucky_button.grid(column=4, row=4)


def first_study_click():
    global study_index, is_luck, click_index, no_power
    is_luck = False
    if student.work_or_chill_decision('first', study_index) == 1:
        main_text.configure(text=text.study_choices[study_index * 2])
    else:
        main_text.configure(text=text.study_choices_without_power[no_power])
        no_power += 1
    study_index += 1
    first_study_button.configure(text=text.first_study_button[study_index])
    second_study_button.configure(text=text.second_study_button[study_index])
    first_study_button.grid_remove()
    second_study_button.grid_remove()
    window.bind("<Button-1>", next_click)


def second_study_click():
    global study_index, is_luck, click_index
    main_text.configure(text=text.study_choices[study_index * 2 + 1])
    is_luck = False
    study_index += 1
    student.work_or_chill_decision('second', study_index)
    first_study_button.configure(text=text.first_study_button[study_index])
    second_study_button.configure(text=text.second_study_button[study_index])
    first_study_button.grid_remove()
    second_study_button.grid_remove()
    window.bind("<Button-1>", next_click)


def first_lucky_click():
    global lucky_index, is_luck, click_index
    if student.luck_decision(lucky_index + 1, 'first'):
        main_text.configure(text=text.lucky_choices[lucky_index * 2])
    else:
        main_text.configure(text=text.lucky_choices[lucky_index * 2 + 1])
    is_luck = True
    lucky_index += 1
    first_lucky_button.configure(text=text.first_lucky_button[lucky_index])
    second_lucky_button.configure(text=text.second_lucky_button[lucky_index])
    first_lucky_button.grid_remove()
    second_lucky_button.grid_remove()
    window.bind("<Button-1>", next_click)


def second_lucky_click():
    global lucky_index, is_luck, click_index
    if student.luck_decision(lucky_index + 1, 'second'):
        main_text.configure(text=text.lucky_choices[lucky_index * 2])
    else:
        main_text.configure(text=text.lucky_choices[lucky_index * 2 + 1])
    is_luck = True
    lucky_index += 1
    first_lucky_button.configure(text=text.first_lucky_button[lucky_index])
    second_lucky_button.configure(text=text.second_lucky_button[lucky_index])
    first_lucky_button.grid_remove()
    second_lucky_button.grid_remove()
    window.bind("<Button-1>", next_click)


window = Tk()
window.title('3 дня до экзамена...')
window.geometry('650x500')
label_text = Label(window, text='3 дня до экзамена...')
main_text = Label(window, text='Начать игру:')
window.bind("<Button-1>", next_click)
first_study_button = Button(window, command=first_study_click, text=text.first_study_button[study_index])
first_lucky_button = Button(window, command=first_lucky_click, text=text.first_lucky_button[lucky_index])
second_study_button = Button(window, command=second_study_click, text=text.second_study_button[study_index])
second_lucky_button = Button(window, command=second_lucky_click, text=text.second_lucky_button[lucky_index])

label_text.grid(column=2, row=0)
main_text.grid(column=2, row=2)
first_study_button.grid(column=0, row=4)
second_study_button.grid(column=4, row=4)
first_study_button.grid_remove()
second_study_button.grid_remove()
window.mainloop()
