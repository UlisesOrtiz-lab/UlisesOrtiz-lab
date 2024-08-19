class DispositivoElectronico:
    def __init__(self, tipo, modelo, especificaciones, precio_compra, origen, garantia):
        self.tipo = tipo  
        self.modelo = modelo  
        self.especificaciones = especificaciones  
        self.precio_compra = precio_compra  
        self.origen = origen  
        self.garantia = garantia  
    
    def calcular_precio_venta(self):
        return self.precio_compra * 1.7

    def mostrar_informacion(self):
        print(f"Tipo: {self.tipo}")
        print(f"Modelo: {self.modelo}")
        print(f"Especificaciones: {self.especificaciones}")
        print(f"Precio de Compra: ${self.precio_compra}")
        print(f"Precio de Venta: ${self.calcular_precio_venta()}")
        print(f"Origen: {self.origen}")
        print(f"Garantía: {self.garantia} meses\n")

celular = DispositivoElectronico(
    tipo="Celular",
    modelo="PHR X1000",
    especificaciones="Pantalla 6.5', 128GB, 4GB RAM, Cámara 48MP",
    precio_compra=300,  
    origen="China",
    garantia=12
)

tablet = DispositivoElectronico(
    tipo="Tablet",
    modelo="PHR T500",
    especificaciones="Pantalla 10', 64GB, 3GB RAM, Batería 6000mAh",
    precio_compra=200,
    origen="China",
    garantia=12
)

portatil = DispositivoElectronico(
    tipo="Portátil",
    modelo="PHR P3000",
    especificaciones="Pantalla 15', 256GB SSD, 8GB RAM, Intel i5",
    precio_compra=600,
    origen="China",
    garantia=24
)

celular.mostrar_informacion()
tablet.mostrar_informacion()
portatil.mostrar_informacion()
