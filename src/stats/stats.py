class Stats:
    def promedio(self, lista):
        return sum(lista) / len(lista) if lista else 0

    def mediana(self, lista):
        if not lista:
            return 0
        s = sorted(lista)
        n = len(s)
        medio = n // 2
        if n % 2 == 0:
            return (s[medio - 1] + s[medio]) / 2
        return float(s[medio])

    def moda(self, lista):
        if not lista:
            return None
        conteo = {}
        for x in lista:
            conteo[x] = conteo.get(x, 0) + 1
        maximo = max(conteo.values())
        for x in lista:
            if conteo[x] == maximo:
                return x

    def varianza(self, lista):
        if not lista:
            return 0
        m = self.promedio(lista)
        return sum((x - m)**2 for x in lista) / len(lista)

    def desviacion_estandar(self, lista):
        return self.varianza(lista) ** 0.5

    def rango(self, lista):
        if not lista:
            return 0
        return max(lista) - min(lista)