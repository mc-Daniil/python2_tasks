# Задача 9/11 — «Ключ меняется»
# Уровень: сложнее | Операции: XOR (^), AND (&), OR (|)
# Ключ зависит от номера позиции. Сдвиги здесь НЕ используются.
# Подсказка: любой символ искомого флага лежит в ASCII (0..127).

TARGET = bytes.fromhex("c3bbb49de9ef928af9d6c1b0fa958fb380c8b3ac85f6aa")


def key_for(i):
    return (0x35 + 19 * i) & 0x7F


def encode(s):
    result = []
    for i, code in enumerate(s.encode("ascii")):
        key = key_for(i)
        value = ((code ^ key) & 0x7F) | 0x80
        result.append(value)
    return bytes(result)


def valid_flag(s):
    """В ответе должны быть только строчные шестнадцатеричные символы."""
    if not s.startswith("vsosh{") or not s.endswith("}"):
        return False
    inner = s[6:-1]
    return len(inner) == 16 and all(c in "0123456789abcdef" for c in inner)


def check(candidate):
    if not valid_flag(candidate):
        return False
    return encode(candidate) == TARGET


if __name__ == "__main__":
    print("Задача 9: ключ меняется")
    print("Изучи encode() и константы TARGET; восстанови исходный флаг.")
    print("Формат: vsosh{{строчные_символы_0-9a-f}}")
    answer = input("Флаг: ").strip()
    print("Верно!" if check(answer) else "Пока неверно. Попробуй обратить алгоритм.")
