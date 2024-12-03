text1 = input("Введіть перше слово:")
text2 = input("Введіть друге слово:")

text1 = list(text1.replace(" ", "").lower())
text2 = list(text2.replace(" ", "").lower())

if sorted(text1) == sorted(text2):
    print("Анаграми")
else:
    print("Не анаграми")