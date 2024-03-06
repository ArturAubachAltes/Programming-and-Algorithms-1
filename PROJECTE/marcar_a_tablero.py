
# Marcar tablero
def Marcar_On_Qui_1(row, col, player, matriu):
    matriu[row][col] = player


def abiable_sqare_1(row, col, matriu):
    if matriu[row][col] == 0:
        return True
    else:
        return False


def Marcar_On_Qui_2(row, col, modo_de_taula, matriu):
    for i in range(modo_de_taula):
        for j in range(modo_de_taula):
            if matriu[i][j] == 0:
                matriu[i][j], matriu[row][col] = matriu[row][col], matriu[i][j]
    return matriu


def abiable_sqare_2(row, col, player_torn, matriu):
    if matriu[row][col] == 1 and player_torn == 1:
        return True
    elif matriu[row][col] == 2 and player_torn == 2:
        return True
    else:
        return False
