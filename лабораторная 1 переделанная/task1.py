numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Заменить значение пропущенного элемента средним арифметическим
In_None = 0
Summ = 0

for i, number in enumerate(numbers):
    if numbers[i] is None:
        In_None = i
    else:
        Summ += numbers[i]

numbers[In_None] = (Summ / len(numbers))
print("Измененный список:", numbers)
