def es_primo(numero):
    if numero<=1:
        return False
    for i in range (2,int(numero**0.5)+1):
        if numero % i==0:
            return False
    return True
n=int(input("ingresar numero"))
if es_primo(n):
    print("es primo")
else:
    print("no es primo")