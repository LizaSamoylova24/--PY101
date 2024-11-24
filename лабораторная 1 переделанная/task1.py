numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Заменить значение пропущенного элемента средним арифметическим
in_None = 0
summ = 0

for i, number in enumerate(numbers):
    if numbers[i] is None:
        in_None = i
    else:
        summ += numbers[i]

numbers[in_None] = (summ / len(numbers))
print("Измененный список:", numbers)
