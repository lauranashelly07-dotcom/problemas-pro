def sumatoria(lista):
    total=0
    for numero in lista:
        total+=numero
        return total
def promedio(lista):
    if not lista:
        return 0
    resultado_suma=sumatoria(lista)
    total_elementos=len(lista)
    return resultado_suma/total_elementos

numeros=[1,2,3,4]
resultado=promedio(numeros)
print(f"la lista es",numeros)
print(f"El promedio es",resultado)