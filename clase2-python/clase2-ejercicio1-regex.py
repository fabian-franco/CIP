try:
    name = str(input("Ingresa tu nombre: "))
    age = int(input("Ingresa tu edad: "))

    vocalRegex = r'[aeiouAEIOU]'
    consonantRegex = r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]'

    if age < 18 and name[0] in vocalRegex:
        print(f"Tu nombre pertenece al grupo 1")
    elif age >= 18 and name[0] in consonantRegex:
        print(f"Tu nombre pertenece al grupo 2")
    else:
        print(f"Tu nombre pertenece al grupo 3")
except:
    print("Ingresa valores validos")