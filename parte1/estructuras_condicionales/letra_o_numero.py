caracter = input("Ingrese carácter: ")

if caracter.isnumeric():
    print("Es número.")
elif caracter.isalpha() and caracter.islower():
    print("Es una letra minúscula.")
elif caracter.isalpha() and caracter.isupper():
    print("Es una letra mayúscula.")
else:
    print("No es ni letra ni número.")
