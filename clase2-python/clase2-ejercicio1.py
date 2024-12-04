try:
    name = str(input("Ingresa tu nombre: "))
    age = int(input("Ingresa tu edad: "))

    groupVocals = ['a', 'e', 'i', 'o', 'u']
    groupConsonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    if age < 18 and name.lower()[0] in groupVocals:
        print(f"Tu nombre pertenece al grupo 1")
    elif age >= 18 and name.lower()[0] in groupConsonants:
        print(f"Tu nombre pertenece al grupo 2")
    else:
        print(f"Tu nombre pertenece al grupo 3")
except:
    print("Ingresa valores validos")