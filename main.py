import os
import random

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import BoundedNumericProperty
from kivy.core.window import Window
from kivy.config import Config


Window.clearcolor = (0, 0, 0, 1)
Window.size = (414, 896)



class BoxLayoutExample(BoxLayout):
    global d_en
    d_en = ["actor", "airport", "angry", "attic", "baby", "bank", "basement", "beach", "bedroom", "bored", "box", "boyfriend", "Brazil", "busy", "Canada", "child", "China", "class", "classmate", "cold", "computer", "day off", "dress", "duty free store", "egg"]
    global d_ua
    d_ua = ["Актор", "Аеропорт", "Сердитий, Злий", "Горище", "Немовля", "Банк", "Підвал", "Пляж", "Спальня", "Нудьгуючий", "Коробка, Ящик", "Хлопець", "Бразилія", "Зайнятий", "Канада", "дитина", "Китай", "заняття, клас", "однокласник", "холодний, холодно", "Компютер", "вихідний", "сукня", "Магазин безмитних товарів", "яйце"]

    global sheet_rows
    sheet_rows = len(d_en)

    rand_num = random.randrange(sheet_rows)
    actual_num = StringProperty(str(rand_num))

    translate = d_ua[rand_num]
    correct = d_en[rand_num]

    translatebel_word = StringProperty(str(translate).capitalize())
    correct_word = StringProperty(str(correct).capitalize())

    my_text_input = StringProperty("")

    answer = StringProperty("")

    def on_button_next(self, widget):
        new_rand_num = random.randrange(sheet_rows)
        word = d_ua[new_rand_num]
        correct_w = d_en[new_rand_num]
        # print(new_rand_num)
        # print(word)
        # print(correct_w)
        self.actual_num = str(new_rand_num)
        self.translatebel_word = str(word.capitalize())
        self.correct_word = str(correct_w.capitalize())
        self.my_text_input = ""
        self.answer = ""
        widget.text = ""

    def on_button_check(self, widget):
        data = widget.text.capitalize()
        correct_word = self.correct_word.capitalize()
        if data == correct_word:
            self.answer = 'Good, go next'
        else:
            self.answer = 'Correct: ' + correct_word

    def clear_filds(self, widget):
        widget.text = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class DictiApp(App):
    pass

DictiApp().run()