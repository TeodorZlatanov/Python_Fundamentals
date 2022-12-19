user_command = input()
coffee_count = 0

while user_command != "END":

    if user_command == "movie" or user_command == "dog" or user_command == "cat" or user_command == "coding":
            coffee_count += 1
            user_command = input()
    elif user_command == "MOVIE" or user_command == "DOG" or user_command == "CAT" or user_command == "CODING":
            coffee_count += 2
            user_command = input()
    else:
        user_command = input()
        continue

if coffee_count > 5:
    print(f"You need extra sleep")
else:
    print(coffee_count)