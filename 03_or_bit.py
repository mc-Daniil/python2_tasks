# Задача 3/11 — «Лишняя единица»
# Уровень: средний | Операция: OR (|)
# encode() ставит один и тот же бит во всех байтах.
# Важно: исходный флаг записан обычными ASCII-символами.

TARGET = bytes.fromhex("f6f3eff3e8fbb1e3b3b3e4b6b8b1b4b3b5b5b2b4fd")


def encode(s):
    return bytes(code | 0x80 for code in s.encode("ascii"))


def valid_flag(s):
    """В ответе должны быть только строчные шестнадцатеричные символы."""
    if not s.startswith("vsosh{") or not s.endswith("}"):
        return False
    inner = s[6:-1]
    return len(inner) == 14 and all(c in "0123456789abcdef" for c in inner)


def check(candidate):
    if not valid_flag(candidate):
        return False
    return encode(candidate) == TARGET


if __name__ == "__main__":
    print("Задача 3: лишняя единица")
    print("Изучи encode() и константы TARGET; восстанови исходный флаг.")
    print("Формат: vsosh{{строчные_символы_0-9a-f}}")
    answer = input("Флаг: ").strip()
    print("Верно!" if check(answer) else "Пока неверно. Попробуй обратить алгоритм.")
