class Data:
    def invertir_lista(self, lista):
        return lista[::-1]

    def buscar_elemento(self, lista, valor):
        try:
            return lista.index(valor)
        except ValueError:
            return -1

    def eliminar_duplicados(self, lista):
        resultado = []
        for x in lista:
            if not any(type(x) == type(v) and x == v for v in resultado):
                resultado.append(x)
        return resultado

    def merge_ordenado(self, lista1, lista2):
        return sorted(lista1 + lista2)

    def rotar_lista(self, lista, n):
        if not lista:
            return []
        n = n % len(lista)
        if n == 0:
            return lista[:]
        return lista[-n:] + lista[:-n]

    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        suma_esperada = n * (n + 1) // 2
        return suma_esperada - sum(lista)

    def es_subconjunto(self, lista1, lista2):
        return all(x in lista2 for x in lista1)

    def implementar_pila(self):
        pila = []
        return {
            "push": lambda x: pila.append(x),
            "pop": lambda: pila.pop(),
            "peek": lambda: pila[-1],
            "is_empty": lambda: len(pila) == 0
        }

    def implementar_cola(self):
        cola = []
        return {
            "enqueue": lambda x: cola.append(x),
            "dequeue": lambda: cola.pop(0),
            "peek": lambda: cola[0],
            "is_empty": lambda: len(cola) == 0
        }

    def matriz_transpuesta(self, matriz):
        if not matriz:
            return []
        return [list(fila) for fila in zip(*matriz)]