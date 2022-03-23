class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro, ):
        self.modelo = modelo
        self.precio = precio
        self.asientos = list(asientos)
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        a = 0
        for i in self.asientos:
            if self.asientos[i] != Asiento:
                a += 1
        return a

    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for j in self.asientos:
                if j != None:
                    if self.registro != j.registro:
                        return "Las piezas no son originales"
                else:
                    continue
            return "Aunto original"
        else:
            return "Las piezas no son originales"


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegristro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo

    
class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco":
            self.color = color
