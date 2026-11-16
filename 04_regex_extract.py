# Задача 4/11 — «ID из журнала»
# Тема: re.findall, захватывающие группы.
# В журнале много полей id=..., но нас интересуют именно числа.
# Найди все значения id и соедини их знаком '-'. Ответ: vsosh{...}.

import re

LOG = "user=anna; id=12; role=guest | id=407; status=ok | id=9"
TARGET = "vsosh{12-407-9}"


def check(answer):
    return answer == TARGET


if __name__ == "__main__":
    print("Извлеки все числа после id= и собери флаг: vsosh{число-число-число}")
    print("LOG:", LOG)
    print("Верно!" if check(input("Флаг: ").strip()) else "Неверно")
