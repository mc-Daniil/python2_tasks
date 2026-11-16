# Задача 7/11 — «Байты по кругу»
# Тема: циклический сдвиг 8-битных чисел.
# Каждый байт флага циклически сдвинут влево на 3 бита.

TARGET = bytes.fromhex("b3 9b 7b 9b 43 db 93 7b a3 0b a3 2b fa 13 4b a3 9b eb")


def rol8(x, n):
    n %= 8
    return ((x << n) | (x >> (8 - n))) & 0xFF


def encode(text):
    return bytes(rol8(b, 3) for b in text.encode("ascii"))


def check(answer):
    return answer.startswith("vsosh{") and answer.endswith("}") and encode(answer) == TARGET


if __name__ == "__main__":
    print("TARGET:", TARGET.hex())
    print("Восстанови исходный флаг vsosh{...}")
    print("Верно!" if check(input("Флаг: ").strip()) else "Неверно")
