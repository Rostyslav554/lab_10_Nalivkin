def calculate_life_number():
    while True:
        try:
            date = input("Введіть дату народження у форматі YYYYMMDD, MMDDYYYY, або будь-якому іншому: ")

            date = ''.join(filter(str.isdigit, date))

            if not date:
                raise ValueError("Введена дата містить лише нецифрові символи. Спробуйте ще раз.")

            while len(date) > 1:
                total = sum(int(digit) for digit in date)
                date = str(total)

            print(f"Цифра життя: {date}")
            break

        except ValueError as e:
            print(f"Помилка: {e}. Будь ласка, введіть правильну дату.")

calculate_life_number()
