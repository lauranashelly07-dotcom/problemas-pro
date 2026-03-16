def validar_email(email):
    if "@" in email:
        return True
    else:
        return False
direccion=input("ingresar direccion de email:")
es_valida=validar_email(direccion)
if es_valida:
    print("es valido")
else:
    print("no es valido")