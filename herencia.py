class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


class Cliente(Persona):
    def __init__(self, nombre, apellido, edad, estadoCuenta):
        self.estadoCuenta = estadoCuenta
        super().__init__(nombre, apellido, edad)
   

    def __str__(self):
        return f"""
        NOMBRE: {self.nombre}
        APELLIDO: {self.apellido}
        EDAD: {self.edad}
        ESTADO DE CUENTA: {self.estadoCuenta}"""

    def depositar(self):
        cantidad = int(input("ingrese la cantidad que desea depositar a su cuenta"))
        self.estadoCuenta = self.estadoCuenta + cantidad

    def Retirar(self):
        cantidad = int(input("ingrese la cantidad que desea retirar a su cuenta"))
        if cantidad < self.estadoCuenta:
            self.estadoCuenta = self.estadoCuenta - cantidad
        else:
            print(f"elige unacantidad correcta menor a {self.estadoCuenta}")


# _____________________________________________________________________________________________________________

nombre = input("ingrese su nombre")
apellido = input("ingrese su apellido")
edad = int(input("ingrese su edad"))
dinero = int(input("ingrese su dinero"))

cliente1 = Cliente(nombre, apellido, edad, dinero)
salir = "x"
while salir != True:
    opcion = int(input("""
                        [1] ----- consultar informacion
                        [2] ----- depositar saldo
                        [3] ----- retirar dinero
                        [4] salir"""))
    if opcion == 1:
        print(cliente1)
    elif opcion == 2:
        cliente1.depositar()
    elif opcion == 3:
        cliente1.Retirar()

    elif opcion == 4:
        salir = True
