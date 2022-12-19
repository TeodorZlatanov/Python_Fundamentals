input_string = input()
final_word = ''

while input_string != "End":

    if input_string == "SoftUni":
        input_string = input()
        continue
    for i in input_string:
        final_word += i * 2

    print(final_word)
    final_word = ''
    input_string = input()