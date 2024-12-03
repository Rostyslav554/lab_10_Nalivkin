def ispalindrom(text):
    text = text.replace(" ", "").lower()
    if text == text[::-1]:
        print("It's a palindrom")
    else:
        print("It's not a palindrom")

text = input("Введіть текст:")
ispalindrom(text)

text = input("Введіть текст:")
ispalindrom(text)