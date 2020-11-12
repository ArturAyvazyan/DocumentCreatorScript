import os
import urllib
import logging
import lpod
import random
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
        print('Введите свое имя')
        self.your_name = input()

        print('Время начала шторма')
        print('Часы')
        self.since_hour = input()
        print('Минуты')
        self.since_minute = input()

        print('Время окончания шторма')
        print('Часы')
        self.to_hour = input()
        print('Минуты')
        self.to_minute = input()

        print('Введите название полигона')
        self.polygon = input()

        print('Влияние какого фронта(холодного, теплого и т.д.)')
        self.front = input()
        print('Откуда дует ветер?(севера/юга и т.д.)')
        self.wind = input()
        print('Облачность в баллах')
        self.cloud = input()
        print('Состояние облачности(кучевая ит.д.)')
        self.wheather = input()
        print('Тип осадков')
        self.rain = input()
        print('Видимость от (в метрах)')
        self.see_1 = input()
        print('Видимость до (в метрах)')
        self.see_2 = input()

        print('Как назовем файл')
        self.file_name = input()

        self.list = ['first', 'second', 'third', 'fourth',
                     'five', 'six', 'seven', 'eight']

        # Файл с информацией о введенных данных.
        logging.basicConfig(level=logging.DEBUG, filename="input_date.log")
        logging.debug('Logging: %s', {'name': self.your_name, 'storm begins(hour)': self.since_hour, 'storm begins(minute)': self.since_minute, 'storm ends(hour)': self.to_hour, 'storm ends(minute)': self.to_minute,
                                      'polygon': self.polygon, 'front': self.front, 'wind': self.wind, 'cloud': self.cloud, 'wheather': self.wheather, 'rain': self.rain, 'Vidimost ot': self.see_1, 'Vidimost do': self.see_2, 'filename': self.file_name})

    def create_doc(self):  
        header = odf_create_heading(0, f'ШТОРМ ПРЕДУПРЕЖДЕНИЕ №{self.rand_2}', True)
        self.body.append(header)

        self.list[0] = odf_create_paragraph(
            f'1: В период с «{self.since_hour}.{self.since_minute}» часов до «{self.to_hour}.{self.to_minute}» часов.')

        self.list[1] = odf_create_paragraph(f'2: По району: {self.polygon}')

        self.list[2] = odf_create_paragraph(
            f'3: Ожидается: В связи с влиянием {self.front} фронта c {self.wind}. Облачность: {self.cloud}б, {self.wheather}. {self.rain}. Видимость: {self.see_1}-{self.see_2} метров')

        self.list[3] = odf_create_paragraph(
            f'4: Время составления: «{self.hours}»ч. «{self.minutes}»мин. Подпись составившего: {self.your_name}')

        self.list[4] = odf_create_paragraph(
            f'5: Время вручения: «{self.hours}»ч. «{self.minutes_appended}»мин. Роспись получившего: {self.appenders[0]}')
        self.list[5] = odf_create_paragraph('6: ШТОРМ ПРЕДУПРЕЖДЕНИЕ ПЕРЕДАНО')

        self.list[6] = odf_create_paragraph('7: Фактическое состояние погоды \n')
        self.fact_wheather_1 = odf_create_paragraph(
            f'{int(self.since_hour)+1}часов {self.since_minute} минут: {self.wheather}, {self.rain}. Видимость {self.see_2} метров')
        self.fact_wheather_2 = odf_create_paragraph(
            f'{int(self.to_hour)-1}часов {self.to_minute} минут: {self.wheather}, {self.rain}. Видимость {self.see_1} метров')
        self.list[7] = odf_create_paragraph(
            f'8. ОЦЕНКА: Берем в команду. ПОДПИСЬ ПРОИЗВОДИВШЕГО ОЦЕНКУ {self.your_name}')

        table = odf_create_table("Table 1", width=5, height=8)
        row = odf_create_row()
        row.set_values(["Адрес", "Время передачи",
                        "Способ передачи", "Кто передал", "Кто принял"])
        table.set_row("A1", row)

        row.set_values(["Руководитель работ", f"{self.hours}.{self.minutes}",
                        "лично с вруч.", f"{self.your_name}", f"{self.appenders[0]}"])
        table.set_row("A2", row)

        row.set_values(["Командир", f"{self.hours}.{int(self.minutes)+1}",
                        "лично", f"{self.your_name}", f"{self.appenders[1]}"])
        table.set_row("A3", row)

        row.set_values(
            ["Дежурный по КП", f"{self.hours}.{int(self.minutes)+2}", "ГГС", f"{self.your_name}", f"{self.appenders[2]}"])
        table.set_row("A4", row)

        row.set_values(
            ["Богатырь-930", f"{self.hours}.{int(self.minutes)+3}", "тлф", f"{self.your_name}", f"{self.appenders[3]}"])
        table.set_row("A5", row)

        row.set_values(["Ива-930 (по запросу)",
                        f"{self.hours}.{int(self.minutes)+4}", "тлф", f"{self.your_name}", f"{self.appenders[4]}"])
        table.set_row("A6", row)

        for l in self.list:
            if l != 'seven' and l != 'eight':
                self.body.append(l)

        self.body.append(table)
        self.body.append(self.list[6])
        self.body.append(self.fact_wheather_1)
        self.body.append(self.fact_wheather_2)
        self.body.append(self.list[7])

        if not os.path.exists('jm'):
            os.mkdir('jm')

        self.output = os.path.join('jm', f'{self.file_name}.odt')
        self.document.save(target=self.output, pretty=True)


AK = Akuta()
AK.go()
AK.create_doc()

