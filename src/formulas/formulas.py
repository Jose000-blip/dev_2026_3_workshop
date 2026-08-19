import math

class Formulas:
    def velocidad_media(self, distancia, tiempo):
        return distancia / tiempo

    def mruv_posicion(self, x0, v0, a, t):
        return x0 + v0 * t + 0.5 * a * t**2

    def mruv_velocidad(self, v0, a, t):
        return v0 + a * t

    def fuerza_newton(self, masa, aceleracion):
        return masa * aceleracion

    def energia_cinetica(self, masa, velocidad):
        return 0.5 * masa * velocidad**2

    def energia_potencial(self, masa, altura, gravedad=9.8):
        return masa * gravedad * altura

    def ley_ohm_voltaje(self, corriente, resistencia):
        return corriente * resistencia

    def ley_ohm_corriente(self, voltaje, resistencia):
        return voltaje / resistencia

    def interes_simple(self, capital, tasa, tiempo):
        return capital * tasa * tiempo

    def interes_compuesto(self, capital, tasa, tiempo, n=1):
        return capital * (1 + tasa / n) ** (n * tiempo)

    def discriminante(self, a, b, c):
        return b**2 - 4 * a * c

    def raices_cuadraticas(self, a, b, c):
        d = self.discriminante(a, b, c)
        if d < 0:
            raise ValueError("Discriminante negativo, no hay raíces reales")
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return (max(x1, x2), min(x1, x2))

    def imc(self, peso, altura):
        return peso / (altura ** 2)

    def hipotenusa_pitagoras(self, cateto1, cateto2):
        return math.sqrt(cateto1**2 + cateto2**2)