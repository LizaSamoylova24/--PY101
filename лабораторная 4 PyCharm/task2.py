import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    # Чтение содержимого CSV файла
    with open(INPUT_FILENAME, "r", encoding="utf-8") as n:
        reader = csv.DictReader(n)
        c = [row for row in reader]

    # Сериализация в файл с отступами равными 4
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as u:
        json.dump(c, u, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME, "r", encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")



