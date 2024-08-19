class Articulo:
    def __init__(self, tipo, precio_compra):
        self._tipo = tipo  
        self._precio_compra = precio_compra  
        self._margen_ganancia = 1.30  
        self._precio_venta = self._calcular_precio_venta()

    def _calcular_precio_venta(self):
        return self._precio_compra * self._margen_ganancia

    def mostrar_informacion(self):
        print(f"Tipo: {self._tipo}")
        print(f"Precio de compra: ${self._precio_compra:.2f}")
        print(f"Precio de venta: ${self._precio_venta:.2f}")
        print()

class Cuaderno(Articulo):
    def __init__(self, hojas, precio_compra):
        super().__init__(f"Cuaderno de {hojas} hojas - Marca HOJITAS", precio_compra)

class Lapiz(Articulo):
    def __init__(self, tipo_lapiz, precio_compra):
        super().__init__(f"Lápiz {tipo_lapiz} - Marca Rayas", precio_compra)

cuaderno_50 = Cuaderno(50, 10)
cuaderno_100 = Cuaderno(100, 15)
lapiz_grafito = Lapiz("de grafito", 2)
lapiz_colores = Lapiz("de colores", 3)

cuaderno_50.mostrar_informacion()
cuaderno_100.mostrar_informacion()
lapiz_grafito.mostrar_informacion()
lapiz_colores.mostrar_informacion()
