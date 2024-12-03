def is_subsequence(word, sequence):
    word = word.lower()
    sequence = sequence.lower()

    pos = -1

    for char in word:
        pos = sequence.find(char, pos + 1)
        if pos == -1:
            return "No"

    return "Yes"


word = "dog"
sequence = "vcxzxduybfdsobywuefgas"
print(is_subsequence(word, sequence))

sequence = "vcxzxdcybfdstbywuefsas"
print(is_subsequence(word, sequence))