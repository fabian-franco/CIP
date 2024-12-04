try:
    name = str(input("Ingresa tu nombre: ")).lower()
    country = str(input("Ingresa tu pais de origen: ")).lower()

    if len(name) < 5 and country == 'colombia':
        print(f"Pertenece al grupo Colombia A")
    elif len(name) >= 5 and (country == 'mexico' or country == 'méxico'):
        print(f"Pertenece al grupo México B")
    else:
        print(f"Perteneces a otros grupos")
except:
    print("Ingresa valores validos")