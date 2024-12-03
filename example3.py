date = input("Введіть дату народження у форматі YYYYMMDD:")

while True:
    sum = 0
    for simbol in date:
        sum += int(simbol)

    date = str(sum)

    if len(date) == 1:
        break

print(sum)