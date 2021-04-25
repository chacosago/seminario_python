import PySimpleGUI as sg


def build(player_1, player_2, board_data):
    """
    Construye la ventana del tablero del juego
    """
    layout = [
        [sg.Text("Jugador 1: " + player_1["name"], key="-P1-", text_color="darkblue")],
        [sg.Text("Jugador 2: " + player_2["name"], key="-P2-", text_color="white")],
        [sg.Text("")],
    ]

    for y in range(3):
        layout += [
            [
                sg.Button(board_data[x][y], size=(8, 4), key=f"cell-{x}-{y}")
                for x in range(3)
            ]
        ]

    board = sg.Window("Ta Te Ti").Layout(layout)

    return board