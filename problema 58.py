def llenar_lista(cantidad):
    lista=[]
    for i in range(cantidad):
        numero=int(input(f"ingrese el numero{i+1}"))
        lista.append(numero)
    return lista

mi_lista=llenar_lista(10)
print(mi_lista)