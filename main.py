import math

def calc(x, y):
    term1 = x ** (y / x)
    term2 = (y / math.sqrt(x)) ** (1/3)
    psi = abs(term1 - term2) + (y - x)
    return psi
x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
psi_value = calc(x, y)
print(f"Значение функции ψ: {psi_value}")
