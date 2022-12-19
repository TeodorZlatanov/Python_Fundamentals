budget = float(input())
kg_flour_price = float(input())

pack_eggs_price = 0.75 * kg_flour_price
liter_milk_price = 1.25 * kg_flour_price
quarter_milk_price = 0.25 * liter_milk_price

one_loaf = pack_eggs_price + kg_flour_price + quarter_milk_price
money = budget
count_loafs = 0
colored_eggs_count = 0

while money >= one_loaf:

    money -= one_loaf
    count_loafs += 1
    colored_eggs_count += 3
    if count_loafs % 3 == 0:
        colored_eggs_count -= (count_loafs - 2)

print(f"You made {count_loafs} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {money:.2f}BGN left.")

