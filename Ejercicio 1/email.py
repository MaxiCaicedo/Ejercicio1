class Email:
    def __init__(self):
        self.idCuenta = input("Ingrese ID de cuenta: ")
        self.dominio = input("Ingrese dominio: ")
        self.tipoDominio = input("Ingrese tipo de dominio: ")
        self.contrasena = input("Ingrese contraseña: ")

    def retornaEmail(self):
        return f"{self.idCuenta}@{self.dominio}.{self.tipoDominio}"

    def getDominio(self):
        return self.dominio

    def crearCuenta(self, email):
        if email.dominio == self.dominio:
            return Email()
        else:
            return None
