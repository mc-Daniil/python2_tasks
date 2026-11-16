# Задача 10/11 — «Сколько рукопожатий?»
# Тема: комбинаторика и обратный анализ формулы.
# Число пар среди n участников: C(n,2)=n*(n-1)//2.
# Каждую цифру секретного кода d от 0 до 9 заменили на C(d+2,2).
# Восстанови цифры и составь флаг vsosh{...}.

TARGET = [15, 6, 28, 45, 3, 10, 21, 36]


def encode(text):
    if not text.startswith("vsosh{") or not text.endswith("}"):
        return None
    digits = text[6:-1]
    if len(digits) != len(TARGET) or not digits.isdecimal():
        return None
    return [((int(d) + 2) * (int(d) + 1)) // 2 for d in digits]


def check(answer):
    return encode(answer) == TARGET


if __name__ == "__main__":
    print("Закодированные цифры:", TARGET)
    print("Восстанови флаг vsosh{8_цифр}")
    print("Верно!" if check(input("Флаг: ").strip()) else "Неверно")
