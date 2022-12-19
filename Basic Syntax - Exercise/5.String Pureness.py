number = int(input())
ch1 = "."
ch2 = ","
ch3 = "_"

for i in range(number):

    user_string = input()

    if ch1 in user_string or ch2 in user_string or ch3 in user_string:
        print(f"{user_string} is not pure!")
    else:
        print(f"{user_string} is pure.")