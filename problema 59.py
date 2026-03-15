def calcular_sumatoria(n):
    suma=0
    for i in range(1,n+1):
        suma+=i
    return suma

resultado=calcular_sumatoria(10)
print(f"la sumatoria es:{resultado}")