class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se han depositado {cantidad} en la cuenta de {self.titular}. Saldo actual: {self.saldo}")
    
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print(f"Fondos insuficientes en la cuenta de {self.titular}.")
        else:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad} de la cuenta de {self.titular}. Saldo actual: {self.saldo}")
    
    def consultar_saldo(self):
        print(f"Saldo actual de la cuenta de {self.titular}: {self.saldo}")

# Instanciación
nombre = input("Ingrese el nombre del titular de la cuenta: ")
cuenta = CuentaBancaria(nombre)

cuenta.depositar(float(input("Ingrese cantidad a depositar: ")))
cuenta.retirar(float(input("Ingrese cantidad a retirar: ")))
cuenta.consultar_saldo()

# Este ejercicio aplica los principios de encapsulamiento al mantener el saldo de la cuenta 
# como un atributo privado, que solo puede modificarse a través de los métodos de la clase. 
# La clase encapsula el comportamiento relacionado con las operaciones bancarias, 
# permitiendo que las interacciones con los objetos de esta clase se realicen a través de métodos bien definidos.