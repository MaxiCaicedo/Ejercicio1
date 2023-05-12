import csv
from email import Email

def test():
    # Test creating an instance of Email
    email1 = Email()
    nombre = input("Ingrese nombre ")
    print(f"Estimado {nombre} te enviaremos tus mensajes a la dirección {email1.retornaEmail()}")

    # Test modifying the password
    contraseña_actual = input("Ingrese contraseña actual: ")
    if contraseña_actual == email1.contrasena:
        nueva_contraseña = input("Ingrese nueva contraseña: ")
        email1.contrasena = nueva_contraseña
    else:
        print("Contraseña incorrecta.")

    # Test creating an instance from an email address
    email2 = Email()
    email2_parts = "informatica.fcefn@gmail.com".split("@")
    email2.idCuenta = email2_parts[0]
    email2.dominio = email2_parts[1].split(".")[0]
    email2.tipoDominio = email2_parts[1].split(".")[1]
    email2.contrasena = "contraseña"

    # Test creating accounts from a list of email addresses
    with open("emails.csv") as f:
        for linea in f:
            email_parts = linea.strip().split(",")
            email = Email()
            email.idCuenta = email_parts[0]
            email.dominio = email_parts[1]
            email.tipoDominio = email_parts[2]
            email.contrasena = email_parts[3]
            if email.retornaEmail() != linea.strip():
                print(f"Direccion de email incorrecta: {linea.strip()}")
            else:
                print(f"Cuenta creada para la direccion de email: {linea.strip()}")

    # Test counting the number of Email objects with a given domain
    dominio = input("Ingrese el dominio a buscar: ")
    cuenta = 0
    for i in range(10):
        email = Email()
        if email.dominio == dominio:
            cuenta += 1
    print(f"Se encontraron {cuenta} direcciones de email con el dominio {dominio}.")


if __name__ == "__main__":
    test()
