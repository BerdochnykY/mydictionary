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
from kivy.lang.builder import Builder


Window.clearcolor = (0, 0, 0, 1)
Window.size = (414, 896)

class DictionaryPage(BoxLayout):
    global d_en
    d_en = ["all day long", "animal", "answer", "around the world", "as Santa", "as you can see", "at Christmas",
            "at Christmas time", "at midnight", "BBQ party", "believe", "blond", "bury", "candy", "capital",
            "celebrate", "century", "champagne", "chess", "chicken soup", "close to", "consider", "culture",
            "decorate", "dislike", "dress up", "egg hunt", "enjoy", "fancy", "feel like", "fireworks", "flower",
            "for holidays", "generally", "get together", "give a card", "glass", "good luck", "grape", "Great Britan",
            "happiness", "healthy", "holiday", "I`m quite the opposite", "imagine", "in fact", "in real life", "invent",
            "keep", "kind", "kiss", "launch", "make ke tired", "mice", "miss", "mind", "NY tradition",
            "on Christmas day", "on Easter day", "on Helloween", "on Mother`s day", "on Thanksgiving",
            "on the 4th of July", "on Valentine`s day", "opposite", "part", "piece of paaper", "polka dot",
            "popular", "prefer", "Really?", "round", "Santa Claus", "smoking", "state", "take the subway",
            "the North Pole", "tradition", "tree", "trick-or-treat", "truth", "turkey", "underwear", "vegetarian",
            "what about you?", "wish", "word", "write down", "you`re right"]
    # d_en = ["actor", "attic", "baby"]
    global d_ua
    d_ua = ["весь день напролет", "животное", "ответ", "по всему миру", "в Санту", "как видите", "на Рождество",
            "в Рождественское время", "в полночь", "вечеринка с барбекю", "верить, полагать", "блондин", "сжигать",
            "конфеты", "столица", "праздновать", "век, столетие", "шампанское", "шахматы", "куриный суп",
            "рядом с, недалеко от", "рассматривать, обдумывать", "культура", "украшать", "не нравится",
            "одеваться, переодеваться", "охотиться на Пасхальные яйца", "наслаждаться, получать удовольствие",
            "модный, не простой", "хотеться", "фейерверк", "цветок", "на праздники", "в общем, обычно",
            "собираться вместе", "подарить открытку", "стакан, бокал", "удача, везение", "виноград", "Великобритания",
            "счастье", "здоровый", "праздник", "у меня совершенно наоборот", "представлять себе", "на самом деле",
            "в реальной жизни", "изобретать", "продолжать", "добрый", "целоваать", "запускать", "делать меня уставшим",
            "мыши", "скучать по", "быть против", "новогодние традиции", "на Рождество", "в день Пасхи", "на Хеллоуин",
            "в День матери", "на День Благодарения", "на 4 июля", "в День святого Валентина", "напротив", "часть",
            "отрывок бумаги", "в горошек", "популярный", "предпочитать", "В самом деле?", "круглый", "Дед Мороз",
            "курение", "штат", "ехать на метро", "Северный Полюс", "традиция", "дерево", "угощай или пожалеешь",
            "правда", "индейка", "нижнее белье", "вегетарианец", "А как на счет тебя?", "желание", "слово", "записать",
            "ты прав / Вы правы"]
    # d_ua = ["Актор", "Горище", "Немовля"]

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
        new_len = len(d_en)
        if new_len > 0:
            new_rand_num = random.randrange(new_len)
            word = d_ua[new_rand_num]
            correct_w = d_en[new_rand_num]
            self.actual_num = str(new_rand_num)
            self.translatebel_word = str(word.capitalize())
            self.correct_word = str(correct_w.capitalize())
            self.my_text_input = ""
            self.answer = ""
            widget.text = ""
        else:
            self.answer = "You lernt all words"
        # print(new_rand_num)
        # print(word)
        # print(correct_w)


    def on_button_check(self, widget):
        data = widget.text.capitalize()
        correct_word = self.correct_word.capitalize()
        if data == correct_word:
            self.answer = 'Good, go next'
            correct_words_list.append(widget.text.lower())
        else:
            self.answer = 'Correct: ' + correct_word

    global correct_words_list
    correct_words_list = []

    def delete_words(self):
        print("delete_words|correct_words_list: " + str(correct_words_list))
        for word in correct_words_list:
            print(word, correct_words_list.count(word))
            if correct_words_list.count(word) > 4:
                while word in correct_words_list:
                    correct_words_list.remove(word)
                index = d_en.index(word)
                print("in d_en index: " + str(d_en.index(word)))
                d_en.pop(index)
                d_ua.pop(index)
        print("delete_words|correct_words_list_END: " + str(correct_words_list))


    def clear_filds(self, widget):
        widget.text = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class DictiApp(App):
    pass

DictiApp().run()