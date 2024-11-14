import json


def task() -> float:
    total = 0

    with open("input.json", "r", encoding="utf-8") as file:
        data = json.load(file)

        for item in data:
            score = item.get("score", 0)
            weight = item.get("weight", 0)

            if score and weight:
                total += score * weight

    return round(total, 3)


print(task())
