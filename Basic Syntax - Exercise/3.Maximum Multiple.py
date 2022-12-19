positive_number = int(input())
boundary = int(input())
largest_number = []

for i in range(1, boundary + 1):

    if i % positive_number == 0:
        largest_number.append(i)

print(max(largest_number))
