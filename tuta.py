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


document = odf_new_document('text')
body = document.get_body()
rand_1 = random.randint(10000, 99999)
rand_2 = random.randint(0, 100)

war_dot = odf_create_paragraph(f'В/Ч №{rand_1}')
body.append(war_dot)

month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
              'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
date_time = str(datetime.now()).split(' ')
date_now = str(date_time[0]).split('-')
year = date_now[0]
month = date_now[1]
month_word = month_list[int(month)-1]
day = date_now[2]

date = odf_create_paragraph(day + f' {month_word} ' + year)
body.append(date)

time = date_time[1].split(':')
hours = time[0]
minutes = int(time[1])
minutes_appended = int(time[1]) + 1

appenders = ['Сеин', 'Недров', 'Сидоров', 'Трофимов', 'Толокнов']
print('Cоставляем шторм-предупреждение')
print('Введите свое имя')
your_name = input()

print('Время начала шторма')
print('Часы')
since_hour = input()
print('Минуты')
since_minute = input()

print('Время окончания шторма')
print('Часы')
to_hour = input()
print('Минуты')
to_minute = input()

print('Введите название полигона')
polygon = input()

print('Влияние какого фронта(холодного, теплого и т.д.)')
front = input()
print('Откуда дует ветер?(севера/юга и т.д.)')
wind = input()
print('Облачность в баллах')
cloud = input()
print('Состояние облачности(кучевая ит.д.)')
wheather = input()
print('Тип осадков')
rain = input()
print('Видимость от (в метрах)')
see_1 = input()
print('Видимость до (в метрах)')
see_2 = input()

print('Как назовем файл')
file_name = input()


list = ['first', 'second', 'third', 'fourth', 'five', 'six', 'seven', 'eight']

# Файл с информацией о введенных данных.
logging.basicConfig(level=logging.DEBUG, filename="input_date.log")
logging.debug('Logging: %s', {'name': your_name, 'storm begins(hour)': since_hour, 'storm begins(minute)': since_minute, 'storm ends(hour)': to_hour, 'storm ends(minute)': to_minute,
                              'polygon': polygon, 'front': front, 'wind': wind, 'cloud': cloud, 'wheather': wheather, 'rain': rain, 'Vidimost ot': see_1, 'Vidimost do': see_2, 'filename': file_name})


def storm_doc():  # CОСТАВЛЯЕМ ФАЙЛЫ
    header = odf_create_heading(0, f'ШТОРМ ПРЕДУПРЕЖДЕНИЕ №{rand_2}', True)
    body.append(header)

    list[0] = odf_create_paragraph(
        f'1: В период с «{since_hour}.{since_minute}» часов до «{to_hour}.{to_minute}» часов.')

    list[1] = odf_create_paragraph(f'2: По району: {polygon}')

    list[2] = odf_create_paragraph(
        f'3: Ожидается: В связи с влиянием {front} фронта c {wind}. Облачность: {cloud}б, {wheather}. {rain}. Видимость: {see_1}-{see_2} метров')

    list[3] = odf_create_paragraph(
        f'4: Время составления: «{hours}»ч. «{minutes}»мин. Подпись составившего: {your_name}')

    list[4] = odf_create_paragraph(
        f'5: Время вручения: «{hours}»ч. «{minutes_appended}»мин. Роспись получившего: {appenders[0]}')
    list[5] = odf_create_paragraph('6: ШТОРМ ПРЕДУПРЕЖДЕНИЕ ПЕРЕДАНО')

    list[6] = odf_create_paragraph('7: Фактическое состояние погоды \n')
    fact_wheather_1 = odf_create_paragraph(
        f'{int(since_hour)+1}часов {since_minute} минут: {wheather}, {rain}. Видимость {see_2} метров')
    fact_wheather_2 = odf_create_paragraph(
        f'{int(to_hour)-1}часов {to_minute} минут: {wheather}, {rain}. Видимость {see_1} метров')
    list[7] = odf_create_paragraph(
        f'8. ОЦЕНКА: Берем в команду. ПОДПИСЬ ПРОИЗВОДИВШЕГО ОЦЕНКУ {your_name}')

    table = odf_create_table("Table 1", width=5, height=8)
    row = odf_create_row()
    row.set_values(["Адрес", "Время передачи",
                    "Способ передачи", "Кто передал", "Кто принял"])
    table.set_row("A1", row)

    row.set_values(["Руководитель работ", f"{hours}.{minutes}",
                    "лично с вруч.", f"{your_name}", f"{appenders[0]}"])
    table.set_row("A2", row)

    row.set_values(["Командир", f"{hours}.{int(minutes)+1}",
                    "лично", f"{your_name}", f"{appenders[1]}"])
    table.set_row("A3", row)

    row.set_values(
        ["Дежурный по КП", f"{hours}.{int(minutes)+2}", "ГГС", f"{your_name}", f"{appenders[2]}"])
    table.set_row("A4", row)

    row.set_values(
        ["Богатырь-930", f"{hours}.{int(minutes)+3}", "тлф", f"{your_name}", f"{appenders[3]}"])
    table.set_row("A5", row)

    row.set_values(["Ива-930 (по запросу)",
                    f"{hours}.{int(minutes)+4}", "тлф", f"{your_name}", f"{appenders[4]}"])
    table.set_row("A6", row)

    for l in list:
        if l != 'seven' and l != 'eight':
            body.append(l)

    body.append(table)
    body.append(list[6])
    body.append(fact_wheather_1)
    body.append(fact_wheather_2)
    body.append(list[7])

    if not os.path.exists('gm'):
        os.mkdir('gm')

    output = os.path.join('gm', f'{file_name}.odt')
    document.save(target=output, pretty=True)


storm_doc()
