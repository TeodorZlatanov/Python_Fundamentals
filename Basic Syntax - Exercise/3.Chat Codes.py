number_of_messages = int(input())

for i in range(1, number_of_messages + 1):

    input_number = int(input())

    if input_number == 88:
        print("Hello")
    elif input_number == 86:
        print("How are you?")
    elif input_number < 88:
        print("GREAT")
    elif input_number > 88:
        print("Bye.")