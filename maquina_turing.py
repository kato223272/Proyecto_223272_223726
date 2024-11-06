import time

codigos_falla = {
    "P0101": "Problema en el circuito del medidor de flujo de masa de aire (MAF).",
    "P0171": "Mezcla de combustible demasiado pobre en el banco 1.",
    "P0300": "Fallo de encendido aleatorio o múltiple en el motor.",
    "P0301": "Falla de encendido en el cilindro 1. Causa probable: Bujía defectuosa, bobina de encendido dañada.",
    "P0420": "Eficiencia del sistema de catalizador debajo del umbral en el banco 1.",
    "P0455": "Fuga grande en el sistema de control de emisiones evaporativas.",
    "P0500": "Mal funcionamiento del sensor de velocidad del vehículo.",
    "P0603": "Fallo en el módulo de control interno.",
    "P0705": "Problema en el circuito del sensor de rango de transmisión.",
    "P0740": "Problema en el circuito del embrague del convertidor de par.",
    "P1101": "Problema en el sensor de flujo de aire de entrada.",
    "P1446": "Mal funcionamiento de la válvula de ventilación de control de emisiones.",
    "P1564": "Mal funcionamiento del sistema de control de velocidad crucero."
}

class MaquinaTuring:
    def __init__(self, codigo):
        self.codigo = codigo
        self.estado_actual = "inicio"
        self.cinta = list(codigo)
        self.resultado = ""

    def paso(self):
        if self.estado_actual == "inicio":
            if "".join(self.cinta) in codigos_falla:
                self.estado_actual = "traducir"
            else:
                self.estado_actual = "error"
                self.resultado = "Código de falla no reconocido."

        elif self.estado_actual == "traducir":
            self.resultado = codigos_falla[self.codigo]
            self.estado_actual = "final"

    def es_finalizado(self):
        return self.estado_actual == "final"
    
    def obtener_resultado(self):
        return self.resultado
