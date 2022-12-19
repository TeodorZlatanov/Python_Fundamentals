orders_number = int(input())
overall_total = 0

for order in range(orders_number):

    capsule_price = float(input())
    if capsule_price <= 0 or capsule_price > 100:
        continue
    days = int(input())
    if days < 1 or days > 31:
        continue
    capsules_per_day = int(input())
    if capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    total = capsule_price * days * capsules_per_day
    print(f"The price for the coffee is: ${total:.2f}")
    overall_total += total

print(f"Total: ${overall_total:.2f}")