# Задача 6/11 — «Неизвестный сдвиг»
# Тема: шифр Цезаря и перебор 26 вариантов.
# Сдвиг неизвестен. Известно, что исходный текст — флаг vsosh{...}.
# Сдвигались только латинские буквы, фигурные скобки остались на месте.

TARGET = "yvrvk{fdhvdu}"


def shift(text, n):
    out = ""
    for c in text:
        if "a" <= c <= "z":
            out += chr((ord(c) - ord("a") + n) % 26 + ord("a"))
        else:
            out += c
    return out


def check(answer):
    return answer.startswith("vsosh{") and answer.endswith("}") and any(shift(answer, n) == TARGET for n in range(26))


if __name__ == "__main__":
    print("Зашифрованная строка:", TARGET)
    print("Перебери сдвиги. Формат: vsosh{...}")
    print("Верно!" if check(input("Флаг: ").strip()) else "Неверно")
