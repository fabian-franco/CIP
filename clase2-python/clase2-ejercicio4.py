print("""}
█████╗ ██████╗  █████╗       ███████╗██████╗ ██████╗
██╔══██╗██╔══██╗██╔══██╗      ██╔════╝██╔══██╗██╔══██╗
███████║██████╔╝███████║█████╗█████╗  ██████╔╝██████╔╝
██╔══██║██╔══██╗██╔══██║╚════╝██╔══╝  ██╔══██╗██╔═══╝
██║  ██║██║  ██║██║  ██║      ███████╗██║  ██║██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝      ╚══════╝╚═╝  ╚═╝╚═╝
                By Fabian Franco
""")


menu = """
1. Añadir producto
2. Listar productos
3. Listar productos a quedarse sin stock
4. Eliminar producto
5. Actualizar producto
6. Salir
"""

products = []

def add_product():
    name = str(input("\nIngresa el nombre: ")).lower()
    price = float(input("Ingresa el precio: "))
    quantity = int(input("Ingresa la cantidad:"))

    if quantity < 0:
        print("\nLa cantidad no puede ser negativa")
        return

    if price < 0:
        print("\nEl precio no puede ser negativo")
        return

    if name == "":
        print("\nEl nombre no puede estar vacio")
        return

    for product in products:
        if product['name'] == name:
            print("\nEl producto ya existe")
            return

    products.append({
        'name': name,
        'price': price,
        'quantity': quantity
    })
    print("\nProducto agregado")

def delete_product():
    name = str(input("\nIngresa el nombre del producto a eliminar: ")).lower()
    if name == "":
        print("\nEl nombre no puede estar vacio")
        return

    if len(products) == 0:
        print("\nNo hay productos")
        return

    if not any(product['name'] == name for product in products):
        print("\nEl producto no existe")
        return

    for product in products:
        if product['name'] == name:
            products.remove(product)
            print("\nProducto eliminado")
            return

def update_product():
    name = str(input("\nIngresa el nombre del producto a actualizar: "))
    if name == "":
        print("\nEl nombre no puede estar vacio")
        return

    if len(products) == 0:
        print("\nNo hay productos")
        return

    if not any(product['name'] == name for product in products):
        print("\nEl producto no existe")
        return

    for product in products:
        if product['name'] == name:
            price = float(input("\nIngresa el nuevo precio: "))
            quantity = int(input("Ingresa la nueva cantidad:"))
            if quantity < 0:
                print("\nLa cantidad no puede ser negativa")
                return
            if price < 0:
                print("\nEl precio no puede ser negativo")
                return
            product['price'] = price
            product['quantity'] = quantity
            print("\nProducto actualizado")
            return

def list_products():
    if len(products) == 0:
        print("\nNo hay productos")
        return

    print("\nLista de productos: \n")

    for product in products:
        print(f"Nombre: {product['name']}, Precio: {product['price']}, Cantidad: {product['quantity']}")

def list_products_out_of_stock():
    if len(products) == 0:
        print("\nNo hay productos que esten quedandose sin stock")
        return

    print("\nLista de productos que esten quedandose sin stock: \n")

    for product in products:
        if product['quantity'] < 5:
            print(f"Nombre: {product['name']}, Precio: {product['price']}, Cantidad: {product['quantity']}")


try:
  while True:
    print(menu)
    option = int(input("Ingresa una opción: "))
    if option == 1:
        add_product()
    elif option == 2:
        list_products()
    elif option == 3:
        list_products_out_of_stock()
    elif option == 4:
        delete_product()
    elif option == 5:
        update_product()
    else:
        print("\nBye :)")
        break

except:
    print("Ingresa datos validos.")
