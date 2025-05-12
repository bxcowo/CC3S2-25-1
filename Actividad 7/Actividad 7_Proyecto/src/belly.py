# src/belly.py
# from src.clock import get_current_time

class Belly:
    def __init__(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def reset(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def comer(self, pepinos):
        if isinstance(pepinos, int) or isinstance(pepinos, float):
            if pepinos < 0:
                raise ValueError(f"Valor erroneo: {pepinos}")
            else:
                print(f"He comido {pepinos} pepinos.")
                self.pepinos_comidos += pepinos
        else:
            raise ValueError(f"Valor erroneo: {pepinos}")

    def esperar(self, tiempo_en_horas):
        if tiempo_en_horas > 0:
            self.tiempo_esperado += tiempo_en_horas

    def esta_gruñendo(self):
        # Verificar que ambas condiciones se cumplan correctamente:
        # Se han esperado al menos 1.5 horas Y se han comido más de 10 pepinos
        if self.tiempo_esperado >= 1.5 and self.pepinos_comidos > 10:
            return True
        return False
