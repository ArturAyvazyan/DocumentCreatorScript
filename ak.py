import os
import urllib
import logging
import lpod
import random
import sys
from datetime import datetime
from lpod.paragraph import odf_create_paragraph
from lpod.document import odf_new_document, odf_get_document
from lpod.heading import odf_create_heading
from lpod.container import *
from lpod.style import *
from lpod.table import odf_create_table, odf_create_row, odf_create_cell, odf_create_column
from lpod.list import odf_create_list, odf_create_list_item


class Akuta:

    def go(self):
        self.document = odf_new_document('text')
        self.body = self.document.get_body()
        self.rand_1 = random.randint(10000, 99999)
        self.rand_2 = random.randint(0, 100)

        self.war_dot = odf_create_paragraph(f'В/Ч №{self.rand_1}')
        self.body.append(self.war_dot)

        self.month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                           'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
        self.date_time = str(datetime.now()).split(' ')
        self.date_now = str(self.date_time[0]).split('-')
        self.year = self.date_now[0]
        self.month = self.date_now[1]
        self.month_word = self.month_list[int(self.month)-1]
        self.day = self.date_now[2]

        self.date = odf_create_paragraph(
            self.day + f' {self.month_word} ' + self.year)
        self.body.append(self.date)

        self.time = self.date_time[1].split(':')
        self.hours = self.time[0]
        self.minutes = int(self.time[1])
        self.minutes_appended = int(self.time[1]) + 1
        self.appenders = ['Сеин', 'Недров', 'Сидоров', 'Трофимов', 'Толокнов']

        print('Cоставляем шторм-предупреждение')

    def name_input(self):
        print('Введите свое имя')
        self.your_name = input()

        if (self.your_name is None) or (str(self.your_name).strip() == "") or (str(self.your_name).isspace() == True):
            print('Представьтесь, пожалуйста')
            self.your_name = input()
            if (self.your_name is None) or (str(self.your_name).strip() == "") or (str(self.your_name).isspace() == True):
                sys.exit()
            else:
                pass
        else:
            pass

    def time_input(self):
        print('Время начала шторма')
        print('Часы')
        self.since_hour = input()

        if (self.since_hour is None) or (str(self.since_hour).strip() == "") or (str(self.since_hour).isspace() or int(self.since_hour) not in range(25)) or int(self.since_hour) == 0:
            print('Введите число от 1 до 24')
            self.since_hour = input()
            if (self.since_hour is None) or (str(self.since_hour).strip() == "") or (str(self.since_hour).isspace() or int(self.since_hour) not in range(25)) or int(self.since_hour) == 0:
                sys.exit()
            else:
                pass
        else:
            print(type(self.since_hour))
            pass

        print('Минуты')
        self.since_minute = input()

        if (self.since_minute is None) or (str(self.since_minute).strip() == "") or (str(self.since_minute).isspace() or int(self.since_minute) not in range(61)) or int(self.since_minute) == 0:
            print('Введите число от 1 до 60')
            self.since_hour = input()
            if (self.since_hour is None) or (str(self.since_minute).strip() == "") or (str(self.since_minute).isspace() or int(self.since_minute) not in range(61)) or int(self.since_minute) == 0:
                sys.exit()
            else:
                pass
        else:
            pass

        print('Время окончания шторма')
        print('Часы')
        self.to_hour = input()

        if (self.to_hour is None) or (str(self.to_hour).strip() == "") or (str(self.to_hour).isspace() or int(self.to_hour) not in range(25)) or int(self.to_hour) == 0:
            print('Введите число от 1 до 24')
            self.to_hour = input()
            if (self.to_hour is None) or (str(self.to_hour).strip() == "") or (str(self.to_hour).isspace() or int(self.to_hour) not in range(25)) or int(self.to_hour) == 0:
                sys.exit()
            else:
                pass
        else:
            pass

        print('Минуты')
        self.to_minute = input()

        if (self.to_minute is None) or (str(self.to_minute).strip() == "") or (str(self.to_minute).isspace() or int(self.to_minute) not in range(61)) or int(self.to_minute) == 0:
            print('Введите число от 1 до 60')
            self.to_minute = input()
            if (self.to_minute is None) or (str(self.to_minute).strip() == "") or (str(self.to_minute).isspace() or int(self.to_minute) not in range(61)) or int(self.to_minute) == 0:
                sys.exit()
            else:
                pass
        else:
            pass

    def polygon_input(self):
        print('Введите название полигона')
        self.polygon = input()
        if (self.polygon is None) or (str(self.polygon).strip() == "") or (str(self.polygon).isspace() == True):
            print('Введите название полигона')
            self.polygon = input()
            if (self.polygon is None) or (str(self.polygon).strip() == "") or (str(self.polygon).isspace() == True):
                sys.exit()
            else:
                pass
        else:
            pass

    def front_input(self):
        print('Влияние какого атмосферного фронта имеет место быть?')
        print('А: Теплого \nБ: Холодного')
        accepted_list = ['A', 'a', 'Б', 'б', 'А', 'а']
        self.front = input()
        if (self.front is None) or (str(self.front).strip() == "") or (str(self.front).isspace() == True) or (str(self.front) not in accepted_list):
            print('Введите А или Б')
            self.front = input()
            if (self.front is None) or (str(self.front).strip() == "") or (str(self.front).isspace() == True) or (str(self.front) not in accepted_list):
                sys.exit()
            else:
                pass
        else:
            pass

    def wind_input(self):
        print('Откуда дует ветер?')
        print('\nА: Север \nБ: Юг \nВ: Запад \nГ: Восток \nД: Юго-Запад \nЕ: Юго-Восток \nЖ: Северо-восток \nЗ: Северо-запад')
        accepted_list = ['A', 'a', 'Б', 'б', 'А', 'а', 'B', 'b', 'В',
                         'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'E', 'e', 'Ж', 'ж', 'З', 'з']
        self.wind = input()
        if (self.wind is None) or (str(self.wind).strip() == "") or (str(self.wind).isspace() == True) or (str(self.wind) not in accepted_list):
            print('Выберите вариант ответа')
            self.wind = input()
            if (self.wind is None) or (str(self.wind).strip() == "") or (str(self.wind).isspace() == True) or (str(self.wind) not in accepted_list):
                sys.exit()
            else:
                pass
        else:
            pass

    def cloud_input(self):
        print('Облачность в баллах по шкале от 1 до 10')
        self.cloud = input()
        if (self.cloud is None) or (str(self.cloud).strip() == "") or (str(self.cloud).isspace() or int(self.cloud) not in range(11)) or int(self.cloud) == 0:
            print('Выберите вариант ответа')
            self.cloud = input()
            if (self.cloud is None) or (str(self.cloud).strip() == "") or (str(self.cloud).isspace() or int(self.cloud) not in range(11)) or int(self.cloud) == 0:
                sys.exit()
            else:
                pass
        else:
            pass

    def wheather_input(self):
        print('Классификация облачности(кучевые/волнистые/перламутровые/перистые и другие)')
        self.wheather = input()
        if (self.wheather is None) or (str(self.wheather).strip() == "") or (str(self.wheather).isspace() == True):
            print('Опишите облака')
            self.wheather = input()
            if (self.wheather is None) or (str(self.wheather).strip() == "") or (str(self.wheather).isspace() == True):
                sys.exit()
            else:
                pass
        else:
            pass

    def rain_input(self):
        print('Тип осадков')
        self.rain = input()
        if (self.rain is None) or (str(self.rain).strip() == "") or (str(self.rain).isspace() == True):
            print('Снег или дождь?')
            self.rain = input()
            if (self.rain is None) or (str(self.rain).strip() == "") or (str(self.rain).isspace() == True):
                sys.exit()
            else:
                pass
        else:
            pass

    def vision_input(self):
        print('Видимость от (в метрах)')
        self.see_1 = input()
        if (self.see_1 is None) or (str(self.see_1).strip() == "") or (str(self.see_1).isspace() or int(self.see_1) not in range(10000)) or int(self.see_1) == 0:
            print('Введие число в метрах')
            self.see_1 = input()
            if (self.see_1 is None) or (str(self.see_1).strip() == "") or (str(self.see_1).isspace() or int(self.see_1) not in range(10000)) or int(self.see_1) == 0:
                sys.exit()
            else:
                pass
        else:
            pass

        print('Видимость до (в метрах)')
        self.see_2 = input()
        if (self.see_2 is None) or (str(self.see_2).strip() == "") or (str(self.see_2).isspace() or int(self.see_2) not in range(10000)) or int(self.see_2) == 0:
            print('Введие число в метрах')
            self.see_2 = input()
            if (self.see_2 is None) or (str(self.see_2).strip() == "") or (str(self.see_2).isspace() or int(self.see_2) not in range(10000)) or int(self.see_2) == 0:
                sys.exit()
            else:
                pass
        else:
            pass

    def file_input(self):
        print('Как назовем файл')
        self.file_name = input()
        if (self.file_name is None) or (str(self.file_name).strip() == "") or (str(self.file_name).isspace() == True):
            print('Представьтесь, пожалуйста')
            self.file_name = input()

            if (self.file_name is None) or (str(self.file_name).strip() == "") or (str(self.file_name).isspace() == True):
                sys.exit()
            else:
                pass
        else:
            pass

        self.list = ['first', 'second', 'third', 'fourth',
                     'five', 'six', 'seven', 'eight']


class File():

    def call_methods(self):
        self.AK = Akuta()
        self.AK.go()
        self.AK.name_input()
        self.AK.time_input()
        self.AK.polygon_input()
        self.AK.front_input()
        self.AK.wind_input()
        self.AK.cloud_input()
        self.AK.wheather_input()
        self.AK.rain_input()
        self.AK.vision_input()
        self.AK.file_input()

    def create_doc(self, **kwargs):
        # AK.wheather_input(self)
        header = odf_create_heading(
            0, f'ШТОРМ ПРЕДУПРЕЖДЕНИЕ №{self.AK.rand_2}', True)
        self.AK.body.append(header)

        self.AK.list[0] = odf_create_paragraph(
            f'1: В период с «{self.AK.since_hour}.{self.AK.since_minute}» часов до «{self.AK.to_hour}.{self.AK.to_minute}» часов.')

        self.AK.list[1] = odf_create_paragraph(
            f'2: По району: {self.AK.polygon}')

        self.AK.list[2] = odf_create_paragraph(
            f'3: Ожидается: В связи с влиянием {self.AK.front} фронта c {self.AK.wind}. Облачность: {self.AK.cloud}б, {self.AK.wheather}. {self.AK.rain}. Видимость: {self.AK.see_1}-{self.AK.see_2} метров')

        self.AK.list[3] = odf_create_paragraph(
            f'4: Время составления: «{self.AK.hours}»ч. «{self.AK.minutes}»мин. Подпись составившего: {self.AK.your_name}')

        self.AK.list[4] = odf_create_paragraph(
            f'5: Время вручения: «{self.AK.hours}»ч. «{self.AK.minutes_appended}»мин. Роспись получившего: {self.AK.appenders[0]}')
        self.AK.list[5] = odf_create_paragraph(
            '6: ШТОРМ ПРЕДУПРЕЖДЕНИЕ ПЕРЕДАНО')

        self.AK.list[6] = odf_create_paragraph(
            '7: Фактическое состояние погоды \n')
        self.AK.fact_wheather_1 = odf_create_paragraph(
            f'{int(self.AK.since_hour)+1}часов {self.AK.since_minute} минут: {self.AK.wheather}, {self.AK.rain}. Видимость {self.AK.see_2} метров')
        self.AK.fact_wheather_2 = odf_create_paragraph(
            f'{int(self.AK.to_hour)-1}часов {self.AK.to_minute} минут: {self.AK.wheather}, {self.AK.rain}. Видимость {self.AK.see_1} метров')
        self.AK.list[7] = odf_create_paragraph(
            f'8. ОЦЕНКА: Берем в команду. ПОДПИСЬ ПРОИЗВОДИВШЕГО ОЦЕНКУ {self.AK.your_name}')

        table = odf_create_table("Table 1", width=5, height=8)
        row = odf_create_row()
        row.set_values(["Адрес", "Время передачи",
                        "Способ передачи", "Кто передал", "Кто принял"])
        table.set_row("A1", row)

        row.set_values(["Руководитель работ", f"{self.AK.hours}.{self.AK.minutes}",
                        "лично с вруч.", f"{self.AK.your_name}", f"{self.AK.appenders[0]}"])
        table.set_row("A2", row)

        row.set_values(["Командир", f"{self.AK.hours}.{int(self.AK.minutes)+1}",
                        "лично", f"{self.AK.your_name}", f"{self.AK.appenders[1]}"])
        table.set_row("A3", row)

        row.set_values(
            ["Дежурный по КП", f"{self.AK.hours}.{int(self.AK.minutes)+2}", "ГГС", f"{self.AK.your_name}", f"{self.AK.appenders[2]}"])
        table.set_row("A4", row)

        row.set_values(
            ["Богатырь-930", f"{self.AK.hours}.{int(self.AK.minutes)+3}", "тлф", f"{self.AK.your_name}", f"{self.AK.appenders[3]}"])
        table.set_row("A5", row)

        row.set_values(["Ива-930 (по запросу)",
                        f"{self.AK.hours}.{int(self.AK.minutes)+4}", "тлф", f"{self.AK.your_name}", f"{self.AK.appenders[4]}"])
        table.set_row("A6", row)

        for l in self.AK.list:
            if l != 'seven' and l != 'eight':
                self.AK.body.append(l)

        self.AK.body.append(table)
        self.AK.body.append(self.AK.list[6])
        self.AK.body.append(self.AK.fact_wheather_1)
        self.AK.body.append(self.AK.fact_wheather_2)
        self.AK.body.append(self.AK.list[7])

        if not os.path.exists('jm'):
            os.mkdir('jm')

        self.AK.output = os.path.join('jm', f'{self.AK.file_name}.odt')
        self.AK.document.save(target=self.AK.output, pretty=True)

        # Файл с информацией о введенных данных.
        logging.basicConfig(level=logging.DEBUG, filename="input_date.log")
        logging.debug('Logging: %s', {'name': self.AK.your_name, 'storm begins(hour)': self.AK.since_hour, 'storm begins(minute)': self.AK.since_minute, 'storm ends(hour)': self.AK.to_hour, 'storm ends(minute)': self.AK.to_minute,
                                      'polygon': self.AK.polygon, 'front': self.AK.front, 'wind': self.AK.wind, 'cloud': self.AK.cloud, 'wheather': self.AK.wheather, 'rain': self.AK.rain, 'Vidimost ot': self.AK.see_1, 'Vidimost do': self.AK.see_2, 'filename': self.AK.file_name})


FILL = File()
FILL.call_methods()
FILL.create_doc()

