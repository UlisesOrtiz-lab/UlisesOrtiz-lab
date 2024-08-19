class Perro:
    def __init__(self, nombre, raza, edad, peso, color):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.color = color
        self.estado = "No atendido"
        self.tamano = "Perro grande" if self.peso >= 10 else "Perro pequeño"

    def registrar(self):
        self.estado = "Atendido"

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Color: {self.color}")
        print(f"Tamaño: {self.tamano}")
        print(f"Estado: {self.estado}")

nombre = input("Ingrese el nombre del perro: ")
raza = input("Ingrese la raza del perro: ")
edad = int(input("Ingrese la edad del perro en años: "))
peso = float(input("Ingrese el peso del perro en kg: "))
color = input("Ingrese el color del perro: ")

perro = Perro(nombre, raza, edad, peso, color)

perro.registrar()

perro.mostrar_info()
