# Задача 1/11 — «Один и тот же ключ»
# Уровень: лёгкий | Операция: XOR (^)
# Получен зашифрованный текст. Какая строка была на входе encode()?

KEY = 0x2D
TARGET = bytes.fromhex("5b5e425e4556141c144c141c1d191c4f50")


def encode(s):
    return bytes(code ^ KEY for code in s.encode("ascii"))


def valid_flag(s):
    """В ответе должны быть только строчные шестнадцатеричные символы."""
    if not s.startswith("vsosh{") or not s.endswith("}"):
        return False
    inner = s[6:-1]
    return len(inner) == 10 and all(c in "0123456789abcdef" for c in inner)


def check(candidate):
    if not valid_flag(candidate):
        return False
    return encode(candidate) == TARGET


if __name__ == "__main__":
    print("Задача 1: один и тот же ключ")
    print("Изучи encode() и константы TARGET; восстанови исходный флаг.")
    print("Формат: vsosh{{строчные_символы_0-9a-f}}")
    answer = input("Флаг: ").strip()
    print("Верно!" if check(answer) else "Пока неверно. Попробуй обратить алгоритм.")
