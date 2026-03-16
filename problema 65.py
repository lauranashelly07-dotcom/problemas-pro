def calc_fac(n):
    if n==0 or n==1:
        return 1
    else:
        factorial=1
        for i in range (1,n+1):
            factorial*=1
        return factorial
def main():
    print("escribe numero factorial o 'salir' para terminar")
    contador_numeros=0
    while True:
        entrada=input("ingresar numero entero positivo").lower()
        if entrada=="salir":
            break
        try:
            numero=int(entrada)
            factorial=calc_fac(numero)
            if factorial is not None:
                print(f"el factorial de {numero}({numero}!)es{factorial}")
                contador_numeros+=1
            else:
                print("error")
        except ValueError:
            print("error")
print("total de numeros{contador_numeros}")
ifname =="_main_":
    main()

