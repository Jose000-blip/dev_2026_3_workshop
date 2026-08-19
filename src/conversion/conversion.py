class Conversion:
    def celsius_a_fahrenheit(self, c):
        return c * 9/5 + 32

    def fahrenheit_a_celsius(self, f):
        return (f - 32) * 5/9

    def metros_a_pies(self, m):
        return m * 3.28084

    def pies_a_metros(self, p):
        return p * 0.3048

    def decimal_a_binario(self, n):
        return bin(n)[2:] if n != 0 else "0"

    def binario_a_decimal(self, b):
        return int(b, 2)

    def decimal_a_romano(self, n):
        valores = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),
                   (100,"C"),(90,"XC"),(50,"L"),(40,"XL"),
                   (10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
        resultado = ""
        for valor, simbolo in valores:
            while n >= valor:
                resultado += simbolo
                n -= valor
        return resultado

    def romano_a_decimal(self, s):
        valores = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total = 0
        for i in range(len(s)):
            actual = valores[s[i]]
            if i + 1 < len(s) and actual < valores[s[i+1]]:
                total -= actual
            else:
                total += actual
        return total

    def texto_a_morse(self, texto):
        morse = {
            'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.',
            'G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..',
            'M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.',
            'S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
            'Y':'-.--','Z':'--..',
            '0':'-----','1':'.----','2':'..---','3':'...--','4':'....-',
            '5':'.....','6':'-....','7':'--...','8':'---..','9':'----.'
        }
        if not texto:
            return ""
        return " ".join(morse[c] for c in texto.upper())

    def morse_a_texto(self, codigo):
        morse_inv = {
            '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
            '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
            '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
            '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
            '-.--':'Y','--..':'Z',
            '-----':'0','.----':'1','..---':'2','...--':'3','....-':'4',
            '.....':'5','-....':'6','--...':'7','---..':'8','----.':'9'
        }
        if not codigo:
            return ""
        letras = codigo.split()
        return "".join(morse_inv[l] for l in letras)