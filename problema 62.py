def calificacion_final(c1,c2,c3):
    promedio=(c1+c2+c3)/3
    print(promedio)
    if promedio<7:
        print("te vas a extras")
        return promedio
nota_final=calificacion_final(7,8,9)
print(nota_final)
