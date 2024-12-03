def get_integer_in_range(prompt, min_value, max_value):
    while True:
        try:
            user_input = input(prompt)

            user_input = int(user_input)

            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Error: the value is not within permitted range ({min_value}..{max_value})")

        except ValueError:
            print("Error: wrong input")


result = get_integer_in_range("Будь ласка, введіть число від 1 до 10: ", 1, 10)
print(f"Ви ввели: {result}")
