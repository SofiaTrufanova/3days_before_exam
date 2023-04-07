import globals
import hide_music_imports  # Он прячет вывод при подключении пакета с музыкой
from pygame import mixer
import result_functions
from tkinter import Button, Label, PhotoImage, Tk


class GameWindow:
    """Игровое окно и его методы"""

    def __init__(self):
        self.window = Tk()
        self.window.title('3 дня до экзамена...')
        self.window.geometry('2560x1600')
        self.label_text = Label(self.window, text='3 дня до экзамена...')
        self.main_text = Label(self.window, text='Начать игру:')
        self.window.bind("<Button-1>", self.next_click)
        self.first_study_button = Button(self.window, command=self.first_study_click,
                                         text=globals.Global.first_study_text[globals.Global.study_index])
        self.first_lucky_button = Button(self.window, command=self.first_lucky_click,
                                         text=globals.Global.first_lucky_text[globals.Global.lucky_index])
        self.second_study_button = Button(self.window, command=self.second_study_click,
                                          text=globals.Global.second_study_text[globals.Global.study_index])
        self.second_lucky_button = Button(self.window, command=self.second_lucky_click,
                                          text=globals.Global.second_lucky_text[globals.Global.lucky_index])
        self.bg = PhotoImage(file=globals.Global.path_of_pictures[globals.Global.number_of_picture])
        self.place = Label(self.window, image=self.bg)
        self.place.grid(column=0, row=6, columnspan=5)
        self.label_text.grid(column=2, row=0)
        self.main_text.grid(column=2, row=2)
        self.first_study_button.grid(column=0, row=4)
        self.second_study_button.grid(column=4, row=4)
        self.first_study_button.grid_remove()
        self.second_study_button.grid_remove()

    def picture(self):
        globals.Global.number_of_picture += 1
        bg = PhotoImage(file=globals.Global.path_of_pictures[globals.Global.number_of_picture])
        self.place.configure(image=bg)

    def ticket(self):
        """Выбор билета"""
        if globals.Global.ticket_type == 'easy':
            self.main_text.configure(text='Вы тянете лёгкий билет!')
        elif globals.Global.ticket_type == 'middle':
            self.main_text.configure(text='Вы тянете обычный билет.')
        else:
            self.main_text.configure(text='Вы тянете сложный билет... Это формула Грина.')

    def examiner(self):
        """Выбор экзаменатора"""
        if globals.Global.exam_type == 'easy':
            self.main_text.configure(
                text='Вы сели его расписывать, и тут экзаменатор называет ваше имя. '
                     'Вы оборачиваетесь и смотрите на экзаменатора:'
                     ' он выглядит добрым)')
        elif globals.Global.exam_type == 'middle':
            self.main_text.configure(
                text='Вы сели его расписывать, и тут экзаменатор называет ваше имя.'
                     'Вы оборачиваетесь и смотрите на экзаменатора:'
                     'он выглядит как среднестатистический экзаменатор.')
        else:
            self.main_text.configure(
                text='Вы сели его расписывать, и тут экзаменатор называет ваше имя.'
                     'Вы оборачиваетесь и смотрите на экзаменатора: '
                     'это Иванова...')

    def before_ending(self):
        """Текст перед концовкой"""
        self.main_text.configure(
            text='В итоге Вы рассказываете свой билет экзаменатору. '
                 'Он задаёт вам вопросы и в итоге отпускает вас...')

    def final(self, event):
        """Финальная часть игры"""
        self.label_text.configure(text=globals.Global.key_situations[-1])
        if globals.Global.click_index == globals.Global.SIXTEEN:
            self.ticket()
        if globals.Global.click_index == globals.Global.SEVENTEEN:
            self.examiner()
        if globals.Global.click_index == globals.Global.EIGHTEEN:
            self.before_ending()
        globals.Global.click_index += 1
        if globals.Global.click_index == globals.Global.NINETEEN:
            final_result = max(2, min(globals.Global.student.result, globals.Global.TEN))
            self.label_text.configure(text=globals.Global.result_text[final_result - 2])
            self.main_text.grid_remove()
            self.window.bind("<Button-1>", self.do_nothing)

    def do_nothing(self, event):
        """Ничего не делает"""
        pass

    def ending(self):
        self.first_study_button.grid_remove()
        self.second_study_button.grid_remove()
        self.first_lucky_button.grid_remove()
        self.second_lucky_button.grid_remove()
        globals.Global.student.prepare_for_exam()
        ticket_type = result_functions.type_of_something(globals.Global.student.fatigue)
        exam_type = result_functions.type_of_something(globals.Global.student.fatigue)
        globals.Global.student.result = result_functions.result(exam_type, ticket_type,
                                                                globals.Global.student.knowledge)
        self.window.bind("<Button-1>", self.final)

    def next_click(self, event):
        """Сменяет экран с тектом на экран с выбором"""
        self.window.bind("<Button-1>", self.do_nothing)
        self.main_text.configure(text=globals.Global.main_text[globals.Global.click_index])
        globals.Global.click_index += 1
        self.picture()
        if globals.Global.click_index >= globals.Global.SIXTEEN:
            self.ending()
        else:
            if globals.Global.is_luck:
                self.first_study_button.grid(column=0, row=4)
                self.second_study_button.grid(column=4, row=4)
            elif globals.Global.study_index % 3 == 0:
                self.label_text.configure(text=globals.Global.key_situations[globals.Global.day])
                globals.Global.day += 1
                self.first_study_button.grid(column=0, row=4)
                self.second_study_button.grid(column=4, row=4)
            else:
                self.first_lucky_button.grid(column=0, row=4)
                self.second_lucky_button.grid(column=4, row=4)

    def after_click(self):
        """Убирает кнопки после выбора - делает это после нажатия кнопки выбора"""
        if globals.Global.is_luck:
            globals.Global.lucky_index += 1
            self.first_lucky_button.configure(text=globals.Global.first_lucky_text[globals.Global.lucky_index])
            self.second_lucky_button.configure(text=globals.Global.second_lucky_text[globals.Global.lucky_index])
            self.first_lucky_button.grid_remove()
            self.second_lucky_button.grid_remove()
        else:
            globals.Global.study_index += 1
            self.first_study_button.configure(text=globals.Global.first_study_text[globals.Global.study_index])
            self.second_study_button.configure(text=globals.Global.second_study_text[globals.Global.study_index])
            self.first_study_button.grid_remove()
            self.second_study_button.grid_remove()
        self.window.bind("<Button-1>", self.next_click)

    def first_study_click(self):
        """Нажатие первой кнопки при учебном выборе"""
        if globals.Global.student.work_or_chill_decision('first', globals.Global.study_index) == 1:
            self.main_text.configure(text=globals.Global.study_choices[globals.Global.study_index * 2])
        else:
            self.main_text.configure(text=globals.Global.study_choices_without_power[globals.Global.no_power])
            globals.Global.no_power += 1
        globals.Global.is_luck = False
        self.after_click()

    def second_study_click(self):
        """Нажатие второй кнопки при учебном выборе"""
        self.main_text.configure(text=globals.Global.study_choices[globals.Global.study_index * 2 + 1])
        globals.Global.student.work_or_chill_decision('second', globals.Global.study_index)
        globals.Global.is_luck = False
        self.after_click()

    def first_lucky_click(self):
        """Нажатие первой кнопки при выборе на удачу"""
        if globals.Global.student.luck_decision(globals.Global.lucky_index + 1, 'first'):
            self.main_text.configure(text=globals.Global.lucky_choices[globals.Global.lucky_index * 2])
        else:
            self.main_text.configure(text=globals.Global.lucky_choices[globals.Global.lucky_index * 2 + 1])
        globals.Global.is_luck = True
        self.after_click()

    def second_lucky_click(self):
        """Нажатие второй кнопки при выборе на удачу"""
        if globals.Global.student.luck_decision(globals.Global.lucky_index + 1, 'second'):
            self.main_text.configure(text=globals.Global.lucky_choices[globals.Global.lucky_index * 2])
        else:
            self.main_text.configure(text=globals.Global.lucky_choices[globals.Global.lucky_index * 2 + 1])
        globals.Global.is_luck = True
        self.after_click()

    def music(self):
        "Отвечает за воспроизведение музыки в игре"
        mixer.init()
        mixer.music.load('everlasting-summer.mp3')
        mixer.music.play(-1)

    def play(self):
        """Запуск окна игры и музыки"""
        self.music()
        self.window.mainloop()
