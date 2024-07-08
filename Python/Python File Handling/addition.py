print("Give me two numbers, and I'll add them.")

first_number = input("First number: ")
second_number = input("Second number: ")
try:
    answer = int(first_number)+int(second_number)
except ValueError:
    print("You can't do addition with characters!")
else:
    print(answer)