def ord_crec(lista):
    lista.sort()
    return lista
def ordena_decreciente(lista):
    lista.sort(reverse=True)
    return lista
def elimina_por_indice(lista,indice):
    valor_eliminado=lista.pop(indice)
    return valor_eliminado
def elimina_por_dato(lista,dato):
    lista.remove(dato)
    return lista
def estadisticas(lista):
    if not lista:
        return 0,0,0
    prommedio=sum(lista)/len(lista)
    maximo=max(lista)
    minimo=min(lista)
    return prommedio, maximo, minimo
def main():
    numeros=[2,16,20]
    print("lista original",numeros)
    print("orden creciente",ord_crec)
    print("orden decreciente",ordena_decreciente)
    nueva_lista=elimina_por_dato(numeros,20)
    print("nueva lista al eliminar el 16",nueva_lista)
    prom,v_max,v_min=estadisticas(numeros)
    print("promedio:{prom:.2f}")
    print("valor maximo:{v_max}")
    print("valor minimo:{v_min}")
if __name__=="_main_":
    main()