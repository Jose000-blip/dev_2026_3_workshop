import random

class Games:
    def piedra_papel_tijera(self, j1, j2):
        validos = ["piedra", "papel", "tijera"]
        j1_l, j2_l = j1.lower(), j2.lower()
        if j1_l not in validos:
            return j1
        if j2_l not in validos:
            return j2
        if j1_l == j2_l:
            return "empate"
        gana = {"piedra": "tijera", "papel": "piedra", "tijera": "papel"}
        return "jugador1" if gana[j1_l] == j2_l else "jugador2"

    def adivinar_numero_pista(self, secreto, intento):
        if intento == secreto:
            return "correcto"
        return "muy alto" if intento > secreto else "muy bajo"

    def ta_te_ti_ganador(self, tablero):
        lineas = []
        lineas.extend(tablero)
        lineas.extend([[tablero[r][c] for r in range(3)] for c in range(3)])
        lineas.append([tablero[i][i] for i in range(3)])
        lineas.append([tablero[i][2-i] for i in range(3)])

        for linea in lineas:
            if linea[0] != " " and linea[0] == linea[1] == linea[2]:
                return linea[0]

        if all(celda != " " for fila in tablero for celda in fila):
            return "empate"
        return "continua"

    def generar_combinacion_mastermind(self, longitud, colores):
        return [random.choice(colores) for _ in range(longitud)]

    def validar_movimiento_torre_ajedrez(self, fila_ini, col_ini, fila_fin, col_fin, tablero):
        if not (0 <= fila_ini < 8 and 0 <= col_ini < 8 and 0 <= fila_fin < 8 and 0 <= col_fin < 8):
            return False
        if fila_ini == fila_fin and col_ini == col_fin:
            return False
        if fila_ini != fila_fin and col_ini != col_fin:
            return False

        if fila_ini == fila_fin:
            paso = 1 if col_fin > col_ini else -1
            for c in range(col_ini + paso, col_fin, paso):
                if tablero[fila_ini][c] != " ":
                    return False
        else:
            paso = 1 if fila_fin > fila_ini else -1
            for f in range(fila_ini + paso, fila_fin, paso):
                if tablero[f][col_ini] != " ":
                    return False
        return True