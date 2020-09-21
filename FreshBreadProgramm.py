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

<CustomDropdown@DropDown>:
    id: dropdown
    on_select:
        app.root.current_screen.ids.date.text = '{}'.format(args[1])
        self.dismiss()
    Button:
        id: btn1
        text: '01/01/20'
        size_hint_y: None
        height: '40dp'
        background_color: (.59, .59, .59, 1)
        background_normal: ''
        background_down: ''
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Line:
                width: 2
                rectangle: self.x, self.y, self.width, self.height
        on_release:
            dropdown.select(btn1.text)
    Button:
        id: btn2
        text: '01/02/20'
        size_hint_y: None
        height: '40dp'
        background_color: (.59, .59, .59, 1)
        background_normal: ''
        background_down: ''
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Line:
                width: 1.5
                rectangle: self.x, self.y, self.width, self.height
        on_release:
            dropdown.select(btn2.text)            
    Button:
        id: btn3
        text: '01/03/20'
        size_hint_y: None
        height: '40dp'
        background_color: (.59, .59, .59, 1)
        background_normal: ''
        background_down: ''
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Line:
                width: 1.5
                rectangle: self.x, self.y, self.width, self.height
        on_release:
            dropdown.select(btn3.text)
    Button:
        id: btn4
        text: '01/04/20'
        size_hint_y: None
        height: '40dp'
        background_color: (.59, .59, .59, 1)
        background_normal: ''
        background_down: ''
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Line:
                width: 1.5
                rectangle: self.x, self.y, self.width, self.height
        on_release:
            dropdown.select(btn4.text) 
    Button:
        id: btn5
        text: '01/05/20'
        size_hint_y: None
        height: '40dp'
        background_color: (.59, .59, .59, 1)
        background_normal: ''
        background_down: ''
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Line:
                width: 1.5
                rectangle: self.x, self.y, self.width, self.height
        on_release:
            dropdown.select(btn5.text) 
    Button:
        id: btn6
        text: '01/06/20'
        size_hint_y: None
        height: '40dp'
        background_color: (.59, .59, .59, 1)
        background_normal: ''
        background_down: ''
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Line:
                width: 1.5
                rectangle: self.x, self.y, self.width, self.height
        on_release:
            dropdown.select(btn6.text) 

<AddNoteScreen>:
    id: addnotescreen
    on_enter:
        root.enter_screen(app.user)
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: ''
    FloatLayout:
        Label:
            id: title
            text: '[color=#010000]Введите дату и кол-во поставленного хлеба (в кг)[/color]'
            markup : True
            font_size : '20sp'
            size_hint: (1, .1)
            halign: 'left'
            pos_hint: {'x':0, 'y':.7}
        DataInput:
            id: date
            text: '01/01/20'
            size_hint:(.45, .05)
            pos_hint:{'x':.27, 'y':.6}
            multiline:False
        Button:
            id: btn
            text: 'v'
            size_hint:(.1, .05)
            pos_hint:{'x':.73, 'y':.6}
            background_color: (.69, .69, .69, 1)
            background_normal: ''
            background_down: ''
            on_press:
                root.dropdown_press()
            on_release:
                Factory.CustomDropdown().open(self)
                root.dropdown_release()

        FloatInput:
            id: liters
            text: '0.0'
            size_hint:(.45, .05)
            pos_hint:{'x':.27, 'y':.53}
            multiline:False  
        
        Button:
            id: confirm_button
            size_hint: (.22, .05)
            pos_hint: {'x':.27, 'y':.44}
            text: 'Добавить запись'
            on_press: 
                root.confirm(app.user, app.info)
        Button:
            id: delete_button
            size_hint: (.22, .05)
            pos_hint: {'x':.5, 'y':.44}
            text: 'Удалить запись'
            on_press: 
                root.delete(app.user, app.info)
        Button:
            id: report
            size_hint: (.24, .05)
            pos_hint: {'x':.27, 'y':.37}
            text: 'Посмотреть отчёт'
            on_press: 
                root.report()
        Button:
            text: 'Назад'
            size_hint: (.2, .05)
            pos_hint: {'x':.52, 'y':.37}
            on_press:
                app.info = root.exit(app.user, app.info)
        Label:
            id: info_label
            text: ''
            markup : True
            font_size : '16sp'
            size_hint: (1, .1)
            pos_hint: {'x':0, 'y':.3}    
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
            id: username_label
            text: "[b]Пользователь: [/b]"
            markup: True
            font_size: '16sp'
            size_hint: (None, None)
            halign: 'left'
            size: self.texture_size
            pos_hint: {'x':.05, 'y':.9}
            color: (.25, .22, .19, 1)
<ReportScreen>:
    on_enter:
        root.enter_screen(app.user)
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: ''
    FloatLayout:
        Label:
            text: '[color=#010000]Отчёт с графиком[/color]'
            markup : True
            font_size : '20sp'
            size_hint: (1, .1)
            pos_hint: {'x':0, 'y':.85}
        Label:
            text: "[color=#010000]Начальная дата[/color]"
            markup : True
            size_hint: (.2, .1)
            pos_hint: {'x':.14, 'y':.78}            
        Label:
            text: "[color=#010000]Конечная дата[/color]"
            markup : True
            size_hint: (.2, .1)
            pos_hint: {'x':.36, 'y':.78}            
        DataInput:
            id:start_date
            text: '01/01/20'
            size_hint: (.2, .05)
            pos_hint: {'x':.14, 'y':.75}
            multiline: False
        DataInput:
            id:end_date
            text: '01/12/20'
            size_hint: (.2, .05)
            pos_hint: {'x':.36, 'y':.75}  
            multiline: False
        Button:
            id: confirm_report
            text: "Подтвердить"
            size_hint: (.2, .05)
            pos_hint: {'x':.6, 'y':.75}   
            on_press:
                root.give_report(app.user, app.info)  
        Button:
            id: clean_button
            text: 'Удалить все записи'
            size_hint: (.22, .05)
            pos_hint: {'x':.14, 'y':.1}
            on_press:
                root.clean(app.user, app.users, app.info)
        Label:
            id: info_label
            text: '...'
            size_hint: (1, .1)
            pos_hint: {'x':0, 'y':.63} 
            color: (.25, .22, .19, 1)   
        Button:
            text: 'Назад'
            size_hint: (.1, .05)
            pos_hint: {'x':.8, 'y':.1} 
            on_press:
                root.manager.current = 'add'
        Image:
            id: plot
            source: ''
            size_hint: (1, .48)
            pos_hint: {'x':0, 'y':.18} 
            opacity: 0
        Label:
            text: "[i][color=#3E3A37]Утешев Илья - учебная практика[/color][/i]"
            markup: True
            font_size: '14sp'
            size_hint: (.5, .1)
            pos_hint: {'x':.27, 'y':.05}
        Label:
            text: "[color=#3E3A37]ИСП-925[/color]"
            markup: True
            font_size: '14sp'
            size_hint: (.5, .1)
            pos_hint: {'x':.27, 'y':.02}
        Label:
            id: username_label
            text: "[b]Пользователь: [/b]"
            markup: True
            font_size: '16sp'
            size_hint: (None, None)
            halign: 'left'
            size: self.texture_size
            pos_hint: {'x':.05, 'y':.9}
            color: (.25, .22, .19, 1)
""")


def plot(df, img, title=False):
    """
    Принимает df, обьект Image для размещения графика, title (bool)
    Строит график по столбцам date (x), liters (y)
    title - наличие названия графика.
    :return: None
    """
    plt.figure(figsize=(10, 5), tight_layout=True)
    ax = plt.subplot(111)
    sns.set(style="darkgrid")
    plt.plot(df['date'].values,
             df['liters'].values)
    x_ticks = df['date'].values
    x_labels = list(df['date'].values)
    if title:
        ax.set_title('Статистика за всё время')
    plt.xticks(x_ticks, rotation='90', labels=x_labels)
    plt.savefig('.data\\partplot.png', optimize=True, quality=100)
    img.reload()
    img.source = ".data\\partplot.png"
    img.opacity = 1


def sort_df(df):
    """
    Принимает df, сортирует по столбцу 'date'
    :return: df
    """
    df['date'] = df['date'].apply(lambda x: datetime.strptime(x, "%d/%m/%y"))
    df = df.sort_values(by=['date'])
    df['date'] = df['date'].apply(lambda x: x.strftime("%d/%m/%y"))
    df = df.reset_index()
    del df['index']
    df.index.name = 'index'
    df.to_csv('.data\\info.csv', sep=';')
    return df


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


class AddnoteScreen(Screen):

    def enter_screen(self, user):
        """
        Добавление логина в верхний label.
        :return: None
        """
        self.ids.username_label.text = f"[b]Пользователь: {user}[/b]"
        self.ids.info_label.text = ""

    def dropdown_press(self):
        self.ids.btn.background_color = (.49, .49, .49, 1)
        self.ids.btn.background_down = ''

    def dropdown_release(self):
        self.ids.btn.background_color = (.69, .69, .69, 1)
        self.ids.btn.background_down = ''

    def confirm(self, user, info):
        """
        Добавление записи в бд.
        Если с такой датой запись существует - новое кол-во проданного кофе прибавляется к старому.
        :return: None
        """
        try:
            self.date = datetime.strptime(self.ids.date.text, "%d/%m/%y")
        except ValueError:
            self.ids.info_label.text = '[color=#DD1B07]Некорректно введена дата[/color]'
        else:
            self.ids.info_label.text = ''
            self.date = self.date.strftime("%d/%m/%y")
            if self.ids.liters.text == '' or self.ids.liters.text == '.' or float(self.ids.liters.text) == 0:
                self.ids.info_label.text = '[color=#DD1B07]Введите объем[/color]'
            else:
                try:
                    self.index = info[(info['user'] == user) & (info['date'] == self.date)].index[0]
                except IndexError:
                    self.last_index = info.count()[0]
                    info.loc[self.last_index] = {'user': user, 'date': self.date, 'liters': float(self.ids.liters.text)}
                    info.to_csv('.data\\info.csv', sep=';')
                    self.ids.info_label.text = "[color=#3E3A37]Добавлена запись:  дата - {},  объем - {}[/color]".format(
                        self.date, self.ids.liters.text)

                else:
                    self.liters = float(info.loc[self.index, 'liters'])
                    self.liters += float(self.ids.liters.text)
                    self.ids.info_label.text = '[color=#DD1B07]Запись с данной датой уже существует.\nНовый объем ' \
                                               'будет прибавлен к записанному ранее[/color][color=#3E3A37]' \
                                               '\nДата - {},  объем - {}[/color]'.format(self.date, self.liters)
                    info.loc[self.index, 'liters'] = self.liters
                    info.to_csv('.data\\info.csv', sep=';')

        finally:
            self.ids.date.text = '01/01/20'
            self.ids.liters.text = '0.0'

    def check_date(self, user, info):
        """
        Проверка введенной даты
        :return: bool
        """
        try:
            datetime.strptime(self.ids.date.text, "%d/%m/%y")
        except ValueError:
            self.ids.info_label.text = '[color=#DD1B07]Некорректно введена дата[/color]'
            return False
        else:
            self.ids.info_label.text = ''
            try:
                self.index = info[(info['user'] == user) & (info['date'] == self.ids.date.text)].index[0]
            except IndexError:
                self.ids.info_label.text = '[color=#DD1B07]Записи с такой датой нет[/color]'
                return False
            else:
                return True

    def delete(self, user, info):
        """
        Удаление записи из бд.
        :return: None
        """
        if self.check_date(user, info):
            self.ids.info_label.text = '[color=#DD1B07]Запись удалена[/color]'
            info.drop(self.index, inplace=True)
            info.index = range(0, info.count()[0])
            print(info)
            info.index.name = 'index'
            info.to_csv('.data\\info.csv', sep=';')

    def exit(self, user, info):
        self.manager.current = 'login'
        return sort_df(df=info)

    def report(self):
        self.manager.current = 'report'


class ReportScreen(Screen):

    def enter_screen(self, user):
        """
        Добавление логина в верхний label.
        Удаление графика
        :return: None
        """
        self.ids.username_label.text = f"[b]Пользователь: {user}[/b]"
        self.ids.info_label.text = ''
        self.ids.plot.source = ""
        self.ids.plot.opacity = 0

    def give_report(self, user, info):
        """
        Вывод кол-ва проданного кофе за данный промежуток времени.
        Построение графика.
        :return: None
        """
        try:
            self.dt_s = datetime.strptime(self.ids.start_date.text, "%d/%m/%y")
            self.dt_e = datetime.strptime(self.ids.end_date.text, "%d/%m/%y")
            print('СДЕЛАНО')
        except ValueError:
            self.ids.info_label.text = "Некорректно введена дата"
            self.ids.info_label.text = (.87, .08, 0, 1)
        else:
            self.info_part = info.copy()
            print(self.info_part)
            print('ТУТ ОШИБКА')
            self.info_part.date = self.info_part.date.apply(lambda x: datetime.strptime(x, "%d/%m/%y"))
            self.info_part = self.info_part[
                (self.info_part.user == user) & (self.info_part.date >= self.dt_s) & (self.info_part.date <= self.dt_e)]
            self.summ = self.info_part['liters'].sum()
            self.info_part.date = self.info_part.date.apply(lambda x: x.strftime("%d/%m/%y"))
            self.ids.info_label.text = f"С {self.ids.start_date.text} по {self.ids.end_date.text} было поставлено {round(self.summ, 4)} кг хлеба"
            plot(df=self.info_part, img=self.ids.plot)



class FloatInput(TextInput):
    """
    Поле ввода с ограничением на ввод символов - только цифры и точка.
    Для дальнейшего преобразования в float.
    """
    pat = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join([re.sub(pat, '', s) for s in substring.split('.', 1)])
        return super(FloatInput, self).insert_text(s, from_undo=from_undo)


class DataInput(TextInput):
    """
    Поле ввода с ограничением на ввод символов - только цифры и слеш.
    Для дальнейшего преобразования в datetime.
    """
    pat = re.compile('[^0-9//]')

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        s = re.sub(pat, '', substring)
        return super(DataInput, self).insert_text(s, from_undo=from_undo)


sm = ScreenManager(transition=FadeTransition(duration=.4))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(AddnoteScreen(name='add'))
sm.add_widget(ReportScreen(name='report'))


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
