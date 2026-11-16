# Задача 8/11 — «Шифр по модулю 26»
# Тема: остаток, НОД, обратный элемент, affine cipher.
# Для латинских букв a=0, ..., z=25 применили y=(5*x+8)%26.
# Остальные символы, включая фигурные скобки, остались без изменений.
# Подсказка: обратный к 5 по модулю 26 равен 21.

TARGET = "juaur{qaxelip}"  # учебный шифртекст


def encode(text):
    out = ""
    for c in text:
        if "a" <= c <= "z":
            x = ord(c) - ord("a")
            out += chr((5 * x + 8) % 26 + ord("a"))
        else:
            out += c
    return out


def check(answer):
    return answer.startswith("vsosh{") and answer.endswith("}") and encode(answer) == TARGET


if __name__ == "__main__":
    print("Шифртекст:", TARGET)
    print("Восстанови флаг vsosh{...}")
    print("Верно!" if check(input("Флаг: ").strip()) else "Неверно")
