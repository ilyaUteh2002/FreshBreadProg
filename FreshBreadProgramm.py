from kivy.config import Config
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from datetime import datetime
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

Builder.load_string("""
#:import SlideTransition kivy.uix.screenmanager.FadeTransition
#:import Factory kivy.factory.Factory

<LoginScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: ''
    FloatLayout:
        Label:
            id: title_label
            #text: "[b][color=#A6622B]FreshBread Co[/color][/b]"
            text: "[b][color=#010000]~FreshBread~[/color][/b]"
            markup: True
            font_size: '28sp'
            size_hint: (.6, .1)
            pos_hint: {'x':.2, 'y':.85}
        Label:
            text: "[i][color=#3E3A37]Утешев Илья - учебная практика[/color][/i]"
            markup: True
            font_size: '14sp'
            size_hint: (.5, .1)
            pos_hint: {'x':.25, 'y':.1}
        Label:
            text: "[color=#3E3A37]ИСП-925[/color]"
            markup: True
            font_size: '14sp'
            size_hint: (.5, .1)
            pos_hint: {'x':.25, 'y':.07}
        Label:
            id: info_label
            text: ''
            markup: True
            font_size: '18sp'
            size_hint: (.6, .1)
            pos_hint: {'x':.2, 'y':.15} 
        Button:
            id: enter_button
            size_hint: (.2, .06)
            pos_hint: {'x':.3, 'y':.4}
            text: 'ВХОД'
            on_press: 
                app.user=root.log_in(app.users, app.user)
            on_release:
                root.release()  
        Button:
            id: register_button
            size_hint: (.2, .06)
            pos_hint: {'x':.5, 'y':.4}
            text: 'РЕГИСТРАЦИЯ'
            on_press: 
                root.register(app.users, app.user)
            on_release:
                root.release()
        Label:
            text:'[color=#231C0B]Имя пользователя[/color]'
            markup : True
            font_size : '16sp'
            size_hint: (None, None)
            halign: 'left'
            size: self.texture_size
            pos_hint:{'x':.3, 'y':.67} 
        TextInput:
            id: login_enter
            text: ''
            size_hint:(.4, .05)
            pos_hint:{'x':.3, 'y':.6}
            multiline:False  
        Label:
            text:'[color=#231C0B]Пароль[/color]'
            markup : True
            font_size : '16sp'
            size_hint: (None, None)
            halign: 'left'
            size: self.texture_size
            pos_hint: {'x':.3, 'y':.56}
        TextInput:
            id: passw_enter
            text: ''
            size_hint: (.4, .05)
            pos_hint: {'x':.3, 'y':.5}
            multiline: False
            password : True

""")



class LoginScreen(Screen):

    def on_enter(self):
        """
        Очищение полей ввода.
        :return: None
        """
        self.ids.login_enter.text = ''
        self.ids.passw_enter.text = ''
        self.ids.info_label.text = ''

    def log_in(self, users, user):
        """
        Проверка логина и пароля на соответствии инф-и в бд.
        Возвращает имя пользователя
        :return: str
        """
        try:
            temp_passw = users[users.user == self.ids.login_enter.text]['pass'].tolist()[0]
            if temp_passw == self.ids.passw_enter.text:
                self.ids.enter_button.text = 'ВХОД'
                user = self.ids.login_enter.text
                self.manager.current = 'add'
                return user
            else:
                self.ids.info_label.text = '[i][color=#DD1B07]Неверно введен пароль[/color][/i]'
        except KeyError:
            self.ids.info_label.text = '[i][color=#DD1B07]Неверно введен пароль[/color][/i]'
        except IndexError:
            if self.ids.login_enter.text == '':
                self.ids.info_label.text = '[i][color=#DD1B07]Введите имя пользователя[/color][/i]'
            else:
                self.ids.info_label.text = '[i][color=#DD1B07]Пользователь с таким именем не найден[/color][/i]'

    def register(self, users, user):
        """
        Добавление пользователя в бд users.
        :return: None
        """
        try:
            users[users.user == self.ids.login_enter.text]['pass'].tolist()[0]
        except IndexError:
            if self.ids.login_enter.text == '':
                self.ids.info_label.text = '[i][color=#DD1B07]Введите имя пользователя[/color][/i]'
            elif self.ids.passw_enter.text == '':
                self.ids.info_label.text = '[i][color=#DD1B07]Введите пароль пользователя[/color][/i]'
            else:
                self.last_index = users.count()[0]
                users.loc[self.last_index] = {'user': self.ids.login_enter.text, 'pass': self.ids.passw_enter.text}
                self.manager.current = 'add'
            users.to_csv('.data\\users.csv', sep=';')
        else:
            self.ids.info_label.text = '[color=#DD1B07]Пользователь с таким именем уже зарегистрирован[/color]'

    def release(self):
        """
        Измененение цвета кнопок на стандартный
        :return: None
        """
        pass
        # self.ids.enter_button.text = 'ВХОД'
        # self.ids.enter_button.background_normal = ''
        # self.ids.enter_button.background_color = (.94, .66, .39, 1)
        # self.ids.register_button.text = 'Зарегистироваться'
        # self.ids.register_button.background_normal = ''
        # self.ids.register_button.background_color = (.94, .66, .39, 1)



sm = ScreenManager(transition=FadeTransition(duration=.4))
sm.add_widget(LoginScreen(name='login'))


class FreshBreadProgramm(App):

    def build(self):
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
        self.title = 'FreshBread'
        self.icon = '.data\\myicon.png'
        Window.clearcolor = (.94, .82, .75, 1)
        Window.size = (800, 600)
        self.user = ''
        self.users = pd.read_csv('.data\\users.csv', sep=';', index_col=[0])
        self.info = pd.read_csv('.data\\info.csv', sep=';', index_col=[0])
        return sm


if __name__ == "__main__":
    FreshBreadProgramm().run()
