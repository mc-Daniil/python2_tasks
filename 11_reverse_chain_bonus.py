# Задача 11/11 — «Обратная цепочка»
# Уровень: сложный | Операции: XOR (^), AND (&), OR (|), цикл
# Порядок действий важен. Код НЕ использует побитовые сдвиги.
# Ищи способ восстановить байты ПО ОДНОМУ, начиная с правильного края.

TARGET = bytes.fromhex("80a6f0b05c9ce7bf1b2c21163fd0c782e4fcf7706801a950f6")


def swap_nibbles(byte):
    # Переставляет старшую и младшую половинки байта.
    left = (byte & 0xF0) // 16
    right = (byte & 0x0F) * 16
    return left | right


def encode(s):
    previous = 0x42
    result = []
    for i, code in enumerate(s.encode("ascii")):
        key = (0x5B + 37 * i) & 0xFF
        mixed = code ^ key ^ previous
        current = swap_nibbles(mixed)
        result.append(current)
        previous = current
    return bytes(reversed(result))


def valid_flag(s):
    """В ответе должны быть только строчные шестнадцатеричные символы."""
    if not s.startswith("vsosh{") or not s.endswith("}"):
        return False
    inner = s[6:-1]
    return len(inner) == 18 and all(c in "0123456789abcdef" for c in inner)


def check(candidate):
    if not valid_flag(candidate):
        return False
    return encode(candidate) == TARGET


if __name__ == "__main__":
    print("Задача 11: обратная цепочка")
    print("Изучи encode() и константы TARGET; восстанови исходный флаг.")
    print("Формат: vsosh{{строчные_символы_0-9a-f}}")
    answer = input("Флаг: ").strip()
    print("Верно!" if check(answer) else "Пока неверно. Попробуй обратить алгоритм.")
