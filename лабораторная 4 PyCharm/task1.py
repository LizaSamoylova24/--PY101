import json


def task() -> float:
    sum_ = 0

    with open("input.json", "r", encoding="utf-8") as q:
        data = json.load(q)

        for item in data:
            chislo1 = item.get("score", 0)
            chislo2 = item.get("weight", 0)

            if chislo1 and chislo2:
                sum_ += chislo1 * chislo2

    return round(sum_, 3)


print(task())



