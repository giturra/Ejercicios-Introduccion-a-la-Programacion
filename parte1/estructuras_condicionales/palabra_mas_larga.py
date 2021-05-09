word1 = input("Palabra 1: ")
word2 = input("Palabra 2: ")

length1 = len(word1)
length2 = len(word2)

if length1 > length2:
    print("La palabra", word1, "tiene", length1 - length2, "letras más que", word2)
elif length1 < length2:
    print("La palabra", word2, "tiene", length2 - length1, "letras más que", word1)
else:
    print("Las palabras tienen el mismo largo")