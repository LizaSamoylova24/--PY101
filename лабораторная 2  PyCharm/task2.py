salary = 5000
spend = 6000
months = 10
increase = 0.03
total_needed = 0


for month in range(months):
    if month > 0:
        spend *= (1 + increase)

         if spend > salary:
              total_needed += spend - salary
import math
    total_needed = math.ceil(total_needed)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", total_needed )

