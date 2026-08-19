class Magic:
    def fibonacci(self, n):
        if n < 0:
            return None
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

    def secuencia_fibonacci(self, n):
        secuencia = []
        a, b = 0, 1
        for _ in range(n):
            secuencia.append(a)
            a, b = b, a + b
        return secuencia

    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def generar_primos(self, n):
        return [x for x in range(2, n + 1) if self.es_primo(x)]

    def es_numero_perfecto(self, n):
        if n < 2:
            return False
        divisores = [i for i in range(1, n) if n % i == 0]
        return sum(divisores) == n

    def triangulo_pascal(self, filas):
        triangulo = []
        for i in range(filas):
            fila = [1] * (i + 1)
            for j in range(1, i):
                fila[j] = triangulo[i-1][j-1] + triangulo[i-1][j]
            triangulo.append(fila)
        return triangulo

    def factorial(self, n):
        if n < 0:
            return None
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def mcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)

    def suma_digitos(self, n):
        return sum(int(d) for d in str(abs(n)))

    def es_numero_armstrong(self, n):
        digitos = str(n)
        potencia = len(digitos)
        return sum(int(d)**potencia for d in digitos) == n

    def es_cuadrado_magico(self, matriz):
        n = len(matriz)
        if n == 1:
            return True
        suma_esperada = sum(matriz[0])
        for fila in matriz:
            if sum(fila) != suma_esperada:
                return False
        for col in range(n):
            if sum(matriz[fila][col] for fila in range(n)) != suma_esperada:
                return False
        if sum(matriz[i][i] for i in range(n)) != suma_esperada:
            return False
        if sum(matriz[i][n-1-i] for i in range(n)) != suma_esperada:
            return False
        return True