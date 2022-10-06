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
    d_en = ["actor", "airport", "angry", "attic", "baby", "bank", "basement", "beach", "bedroom", "bored", "box",
            "boyfriend", "Brazil", "busy", "Canada", "child", "China", "class", "classmate", "cold", "computer",
            "day off", "dress", "duty free store", "egg", "about", "actually", "admire", "airport",
            "an hour and a half", "around", "around me", "Asia", "at the beginning of", "at the moment", "attend",
            "baby panda", "bake", "beach", "beer", "beginning", "bicycle", "build", "building", "by bicycle",
            "by bus", "by car", "by foot", "by plane", "by subway", "by train", "camell", "capital", "cartoon",
            "central square", "central train station", "certanly", "Christmas lights", "Christmas tree", "climb",
            "close", "coconut", "coffee shop", "country", "cousin", "crocodile", "cute", "decorate", "downtown",
            "enjoy", "Europe", "Excuse me", "famous for", "finish", "flight", "for a good price", "garden", "get",
            "get off", "go around", "half an hour", "hate", "have dinner", "homemade", "Hope you are doing greate!",
            "horse", "hostel", "how far …?", "hug", "in one year", "included", "it`s far away", "juice", "knit", "last",
            "learn", "local", "make dinner", "make new friends", "market", "modern", "mountains", "music festival",
            "national", "offer", "one of these days", "opera house", "palace", "paper", "pasta", "pebble beach",
            "per person", "pie", "place", "plant", "play", "potatoes", "quite normal", "rainforest", "really",
            "restaurant", "ride", "sandy", "see you in a week", "snowy", "souvenir", "souvenir store", "stadium",
            "start", "station", "summer house", "sushi", "sweater", "take a trip", "tea", "the Earth",
            "the Northen Lights", "the other day", "the Sun", "tour", "train", "transfer", "tropical", "US visa",
            "walk", "watch", "what kind of …?", "wounderful", "workout", "yoga", "yoga center"]
    global d_ua
    d_ua = ["Актор", "Аеропорт", "Сердитий, Злий", "Горище", "Немовля", "Банк", "Підвал", "Пляж", "Спальня",
            "Нудьгуючий", "Коробка, Ящик", "Хлопець", "Бразилія", "Зайнятий", "Канада", "дитина", "Китай",
            "заняття, клас", "однокласник", "холодний, холодно", "Компютер", "вихідний", "сукня",
            "Магазин безмитних товарів", "яйце", "около, приблизительно", "на самом деле", "восхищаться", "аэропорт",
            "полтора часа", "около, приблизительно", "вокруг меня", "Азия", "в начале", "в данный момент", "посещать",
            "детеныш панды", "печь", "пляж", "пиво", "начало", "велосипед", "строить", "здание", "на велосипеде",
            "на автобусе", "на машине", "пешком", "на самолете", "на метро", "на поезде", "верблюд", "столица",
            "мультфильм", "центральная площадь", "центральный железнодорожный вокзал", "безусловно",
            "Рождественские огни", "Рождественская елка", "карабкаться, взбираться", "близко", "кокос", "кофейня",
            "страна", "двоюродная сестра", "крокодил", "милый", "украшать", "центр города", "наслаждаться", "Европа",
            "Извините", "известен благодаря", "заканчивать", "рейс", "за хорошую цену", "сад", "добираться, получать",
            "выходить (из транспорта)", "ходить по/вокруг", "полчаса", "ненавидеть", "обедать", "домашний",
            "Надеюсь, у вас все хорошо!", "лошадь", "хостел", "как далеко …?", "обнимать", "за один год", "включен",
            "это далеко", "сок", "вязать", "длиться", "учить", "местный", "готовить обед", "заводить новых друзей",
            "рынок", "современный", "горы", "музыкальный вестиваль", "национальный", "предлагать",
            "на днях (в будущем)", "оперный театр", "дворец", "бумага", "макаронные изделия", "галечный пляж",
            "за человека", "пирог", "место", "посадить", "пьеса", "картофель", "вполне нормально", "тропический лес",
            "действительно", "ресторан", "ездить, кататься на", "песчаный", "увидимся через неделю", "снежный",
            "сувенир", "сувенирный магазин", "стадион", "начать", "станция", "летний дом", "суши", "свитер",
            "совершать поездку", "чай", "Земля", "Северное сияние", "на днях (в прошлом)", "Солнце", "тур", "поезд",
            "трансфер", "тропический", "виза в США", "гулять, ходить", "смотреть", "какого рода/вида/сорта",
            "замечательный, чудесный", "тренировка", "йога", "центр йоги"]

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
        print(new_rand_num)
        print(word)
        print(correct_w)
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