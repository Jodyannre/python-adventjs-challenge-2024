from typing import List, Literal

def main():
    board = ['·····', '*····', '@····', 'o····', 'o····']
    print(move_train(board, 'U'))
    print(move_train(board, 'D'))
    print(move_train(board, 'L'))
    print(move_train(board, 'R'))


#Crash en la pagina no reconoce los for anidados
"""
def move_train(board: List[str], mov: Literal['U', 'D', 'R', 'L']) -> Literal['none', 'crash', 'eat']:
    #Definiciones
    max_row = len(board)
    max_column = len(board[0])
    movements = {'U': [0, -1], 'D': [0, 1], 'R': [1, 0], 'L': [-1, 0]}
    symbols = {'o':'crash','*':'eat','·':'none'}
    crash_positions = [-1,max_row,max_column]

    #Buscar la posición de la cabeza
    head_x,head_y = [(y,x) for x,row in enumerate(board) for y,sym in enumerate(row) if '@' == sym ][0]

    #Actualizar posición de la cabeza
    mov_to_do = movements[mov]
    head_x += mov_to_do[0]
    head_y += mov_to_do[1]

    #Verificar crash con bordes
    if head_x in crash_positions or head_y in crash_positions:
        return 'crash'

    #Verificar estado de la cabeza, encontrar simbolo de resultado
    result = symbols[board[head_y][head_x]]

    return result
"""


#Version 2: Igualmente en la web no funciona, error en la web, algo esta mal

def move_train(board: List[str], mov: Literal['U', 'D', 'R', 'L']) -> Literal['none', 'crash', 'eat']:
    #Definiciones
    max_row = len(board)
    max_column = len(board[0])
    movements = {'U': [0, -1], 'D': [0, 1], 'R': [1, 0], 'L': [-1, 0]}
    symbols = {'o':'crash','*':'eat','·':'none'}
    crash_positions = [-1,max_row,max_column]
    head_x, head_y = [0, 0]

    #Buscar la posición de la cabeza
    for y,row in enumerate(board):
        if '@' in row:
            head_y = y
            head_x = row.index('@')
            break

    #Actualizar posición de la cabeza
    mov_to_do = movements[mov]
    head_x += mov_to_do[0]
    head_y += mov_to_do[1]

    #Verificar crash con bordes
    if head_x in crash_positions or head_y in crash_positions:
        return 'crash'

    #Verificar estado de la cabeza, encontrar simbolo de resultado
    result = symbols[board[head_y][head_x]]

    return result


if __name__ == '__main__':
    main()