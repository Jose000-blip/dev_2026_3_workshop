import re

class Strings:
    def es_palindromo(self, texto):
        limpio = "".join(texto.lower().split())
        return limpio == limpio[::-1]

    def invertir_cadena(self, texto):
        return texto[::-1]

    def contar_vocales(self, texto):
        return sum(1 for c in texto.lower() if c in "aeiou")

    def contar_consonantes(self, texto):
        return sum(1 for c in texto.lower() if c.isalpha() and c not in "aeiou")

    def es_anagrama(self, s1, s2):
        limpio1 = s1.lower().replace(" ", "")
        limpio2 = s2.lower().replace(" ", "")
        return sorted(limpio1) == sorted(limpio2)

    def contar_palabras(self, texto):
        return len(texto.split())

    def palabras_mayus(self, texto):
        return " ".join(p.capitalize() if p else p for p in texto.split(" "))

    def eliminar_espacios_duplicados(self, texto):
        return re.sub(r' {2,}', ' ', texto)

    def es_numero_entero(self, texto):
        if texto.startswith('-'):
            return texto[1:].isdigit() and len(texto) > 1
        return texto.isdigit()

    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for c in texto:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
            else:
                resultado += c
        return resultado

    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, sub):
        if not sub:
            return []
        posiciones = []
        inicio = 0
        while True:
            idx = texto.find(sub, inicio)
            if idx == -1:
                break
            posiciones.append(idx)
            inicio = idx + 1
        return posiciones