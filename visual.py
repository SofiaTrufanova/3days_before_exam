from tkinter import *
import text

click_index = 0
lucky_index = 0
study_index = 0
day = 0
is_luck = False


def final():
    global click_index
    label_text.configure(text=text.key_situations[-1])
    main_text.configure(text=text.main_text[click_index])
    click_index += 1
    if click_index == 19:
        label_text.configure(text='Конец игры.')
        main_text.grid_remove()
        next_button.grid_remove()


def next_click():
    global click_index, lucky_index, study_index, day
    next_button.grid_remove()
    main_text.configure(text=text.main_text[click_index])
    click_index += 1
    if click_index >= 16:
        first_study_button.grid_remove()
        second_study_button.grid_remove()
        first_lucky_button.grid_remove()
        second_lucky_button.grid_remove()
        next_button.configure(command=final)
        next_button.grid()
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
    global study_index, is_luck, click_index
    main_text.configure(text=text.study_choices[study_index * 2])
    is_luck = False
    study_index += 1
    next_button.grid(column=2, row=4)
    first_study_button.configure(text=text.first_study_button[study_index])
    second_study_button.configure(text=text.second_study_button[study_index])
    first_study_button.grid_remove()
    second_study_button.grid_remove()


def second_study_click():
    global study_index, is_luck, click_index
    main_text.configure(text=text.study_choices[study_index * 2 + 1])
    is_luck = False
    study_index += 1
    next_button.grid(column=2, row=4)
    first_study_button.configure(text=text.first_study_button[study_index])
    second_study_button.configure(text=text.second_study_button[study_index])
    first_study_button.grid_remove()
    second_study_button.grid_remove()


def first_lucky_click():
    global lucky_index, is_luck, click_index
    main_text.configure(text=text.lucky_choices[lucky_index * 2])
    is_luck = True
    lucky_index += 1
    next_button.grid(column=2, row=4)
    first_lucky_button.configure(text=text.first_lucky_button[lucky_index])
    second_lucky_button.configure(text=text.second_lucky_button[lucky_index])
    first_lucky_button.grid_remove()
    second_lucky_button.grid_remove()


def second_lucky_click():
    global lucky_index, is_luck, click_index
    main_text.configure(text=text.lucky_choices[lucky_index * 2 + 1])
    is_luck = True
    lucky_index += 1
    next_button.grid(column=2, row=4)
    first_lucky_button.configure(text=text.first_lucky_button[lucky_index])
    second_lucky_button.configure(text=text.second_lucky_button[lucky_index])
    first_lucky_button.grid_remove()
    second_lucky_button.grid_remove()


window = Tk()
window.title('3 дня до экзамена...')
window.geometry('650x500')
label_text = Label(window, text='3 дня до экзамена...')
main_text = Label(window, text='Начать игру:')
next_button = Button(window, text='Дальше ->', command=next_click)
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
next_button.grid(column=2, row=4)
window.mainloop()
