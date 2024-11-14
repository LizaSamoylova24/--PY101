import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Чтение содержимого CSV файла
    with open(INPUT_FILENAME, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

    # Сериализация в файл с отступами равными 4
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as output_file:
        json.dump(data, output_file, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME, "r", encoding="utf-8") as output_file:
        for line in output_file:
            print(line, end="")
