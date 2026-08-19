class Matrix:
    def suma_matrices(self, A, B):
        if len(A) != len(B) or any(len(a) != len(b) for a, b in zip(A, B)):
            raise ValueError("Dimensiones incompatibles")
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    def resta_matrices(self, A, B):
        if len(A) != len(B) or any(len(a) != len(b) for a, b in zip(A, B)):
            raise ValueError("Dimensiones incompatibles")
        return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    def multiplicar_matrices(self, A, B):
        if len(A[0]) != len(B):
            raise ValueError("Dimensiones incompatibles")
        filas_A, cols_A, cols_B = len(A), len(A[0]), len(B[0])
        resultado = [[0]*cols_B for _ in range(filas_A)]
        for i in range(filas_A):
            for j in range(cols_B):
                resultado[i][j] = sum(A[i][k] * B[k][j] for k in range(cols_A))
        return resultado

    def multiplicar_escalar(self, M, escalar):
        return [[x * escalar for x in fila] for fila in M]

    def transpuesta(self, M):
        if not M:
            return []
        return [list(fila) for fila in zip(*M)]

    def es_cuadrada(self, M):
        if not M:
            return False
        return all(len(fila) == len(M) for fila in M)

    def es_simetrica(self, M):
        return M == self.transpuesta(M)

    def traza(self, M):
        if not self.es_cuadrada(M):
            raise ValueError("La matriz no es cuadrada")
        return sum(M[i][i] for i in range(len(M)))

    def determinante_2x2(self, M):
        if len(M) != 2 or len(M[0]) != 2:
            raise ValueError("La matriz no es 2x2")
        return M[0][0]*M[1][1] - M[0][1]*M[1][0]

    def determinante_3x3(self, M):
        if len(M) != 3 or len(M[0]) != 3:
            raise ValueError("La matriz no es 3x3")
        a, b, c = M[0]
        d, e, f = M[1]
        g, h, i = M[2]
        return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)

    def identidad(self, n):
        return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    def diagonal(self, M):
        if not self.es_cuadrada(M):
            raise ValueError("La matriz no es cuadrada")
        return [M[i][i] for i in range(len(M))]

    def es_diagonal(self, M):
        for i in range(len(M)):
            for j in range(len(M[0])):
                if i != j and M[i][j] != 0:
                    return False
        return True

    def rotar_90(self, M):
        return [list(fila) for fila in zip(*M[::-1])]

    def buscar_en_matriz(self, M, valor):
        resultado = []
        for i, fila in enumerate(M):
            for j, x in enumerate(fila):
                if x == valor:
                    resultado.append((i, j))
        return resultado