# Задача 2/11 — «Два кусочка байта»
# Уровень: несложный | Операции: AND (&), OR (|)
# Каждый байт был разделён на две части, но в пустые позиции добавили шум.
# Цель: восстановить исходную строку.

HIGH = bytes.fromhex("7d7d6d7d6d7d3d3d3d3d3d6d3d6d6d3d3d6d7d")
LOW = bytes.fromhex("a6a3afa3a8aba5a9a8a1a3a3a7a3a2a5a6a1ad")
TARGET = (HIGH, LOW)


def encode(s):
    result_high = []
    result_low = []
    for code in s.encode("ascii"):
        result_high.append((code & 0xF0) | 0x0D)
        result_low.append((code & 0x0F) | 0xA0)
    return bytes(result_high), bytes(result_low)


def valid_flag(s):
    """В ответе должны быть только строчные шестнадцатеричные символы."""
    if not s.startswith("vsosh{") or not s.endswith("}"):
        return False
    inner = s[6:-1]
    return len(inner) == 12 and all(c in "0123456789abcdef" for c in inner)


def check(candidate):
    if not valid_flag(candidate):
        return False
    return encode(candidate) == TARGET


if __name__ == "__main__":
    print("Задача 2: два кусочка байта")
    print("Изучи encode() и константы TARGET; восстанови исходный флаг.")
    print("Формат: vsosh{{строчные_символы_0-9a-f}}")
    answer = input("Флаг: ").strip()
    print("Верно!" if check(answer) else "Пока неверно. Попробуй обратить алгоритм.")
