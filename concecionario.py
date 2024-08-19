class Auto:
    def __init__(self, marca, modelo, año, color, tipo_motor, tipo_combustible, tipo_transmision, origen, precio_compra, stock):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.tipo_motor = tipo_motor
        self.tipo_combustible = tipo_combustible
        self.tipo_transmision = tipo_transmision
        self.origen = origen  
        self.precio_compra = precio_compra
        self.stock = stock
        self.precio_venta = self.calcular_precio_venta()
        self.ruedas = 4
        self.capacidad_pasajeros = 5

    def calcular_precio_venta(self):
        return self.precio_compra * 1.4

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Tipo de Motor: {self.tipo_motor}")
        print(f"Tipo de Combustible: {self.tipo_combustible}")
        print(f"Tipo de Transmisión: {self.tipo_transmision}")
        print(f"Origen: {self.origen}")
        print(f"Precio de Compra: ${self.precio_compra}")
        print(f"Precio de Venta: ${self.precio_venta}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Capacidad de Pasajeros: {self.capacidad_pasajeros}")
        print(f"Stock: {self.stock}")

concesionario = []

concesionario.append(Auto("FORD", "Bronco", 2024, "verde jade", "1.8L", "Gasolina", "Automática", "Nacional", 20000, 10))
concesionario.append(Auto("BMW", "Serie 1", 2024, "gris", "2.0L", "Gasolina", "Manual", "Importado", 22000, 5))

for auto in concesionario:
    auto.mostrar_info()
    print("-" * 30)
