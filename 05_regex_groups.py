# Задача 5/11 — «Жадный тег»
# Тема: группы в regex, жадность и нежадный поиск.
# В тексте три тега <code>. Найди содержимое КАЖДОГО тега и склей через '-'.
# Для сравнения попробуй шаблоны .* и .*?

import re

TEXT = "<code>alpha</code><code>beta</code><code>gamma</code>"
TARGET = "vsosh{alpha-beta-gamma}"


def check(answer):
    return answer == TARGET


if __name__ == "__main__":
    print("Достань содержимое трёх тегов <code>. Формат: vsosh{часть-часть-часть}")
    print("TEXT:", TEXT)
    print("Верно!" if check(input("Флаг: ").strip()) else "Неверно")
