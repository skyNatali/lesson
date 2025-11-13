import math

def square(side):
    area = side * side
    if side % 1 == 0:
        return area
    else:
        return math.ceil(area)

# Примеры использования
print(square(5))     # 25
print(square(5.0))   # 25.0
print(square(5.5))   # 31 (т.к. 5.5 * 5.5 = 30.25 → округляем до 31)
