import random 


def password(lontitud:int):
    caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(lontitud):
        password += random.choice(caracteres)
    return password

def tabla(numero:int):
    resultado = ""
    for i in range(1, 11):
        resultado +=  f"{i} X {numero} = {i * numero}\n"
    return resultado




