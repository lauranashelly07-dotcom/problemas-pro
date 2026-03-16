def fil_rep(list_alum):
    nom_rep=[]
    for nombre,cal in list_alum:
        if cal<70:
            nom_rep.append(nombre)
    return nom_rep

d_c=[
    ("sofia",85),
    ("jose",50)
]
resultado=fil_rep(d_c)
print(f"los reprobados son {resultado}")