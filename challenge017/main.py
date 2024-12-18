


def main():
    input1 = [
        [True, False, False],
        [False, True, False],
        [False, False, False],
    ]

    input2 = [
        [True, True],
        [False, False],
        [True, True]
    ]

    input3 = [
        ['1', False],
        [False, False]
    ]

    print(detect_bombs(input1))
    print(detect_bombs(input2))
    print(detect_bombs(input3))


#Pésimo, 1 estrella
def detect_bombs(grid: list[list[bool]]) -> list[list[int]]:
    x_limit = len(grid[0])
    y_limit = len(grid)
    result = [[0] * x_limit for _ in range(y_limit)]
    visited = [[False] * x_limit for _ in range(y_limit)]

    def save(x_new, y_new):
        if 0 <= x_new < x_limit and 0 <= y_new < y_limit:
            result[y_new][x_new] += 1
            if grid[y_new][x_new] == True and grid[y_new][x_new] == '1':
                if not visited[y_new][x_new]:
                    recorrer(x_new, y_new)


    def recorrer(x,y):
        if visited[y][x]:
            return
        for y, row in enumerate(grid):
            for x, column in enumerate(row):
                if grid[y][x] != True and grid[y][x] != '1':
                    continue
                visited[y][x] = True
                for dy in [-1, 0, 1]:
                    if 0 >= y+dy > y_limit:
                        continue
                    for dx in [-1, 0, 1]:
                        if dy == 0 and dx == 0:
                            continue
                        if 0 >= x+dx > x_limit:
                            continue
                        save(x + dx, y + dy)

    recorrer(0,0)
    return result



"""
def detect_bombs(grid: list[list[bool]]) -> list[list[int]]:
    x_limit = len(grid[0])
    y_limit = len(grid)
    result = [[0] * x_limit for _ in range(y_limit)]

    def save(x_new, y_new):
        if 0 <= x_new < x_limit and 0 <= y_new < y_limit:
            result[y_new][x_new] += 1

    for y, row in enumerate(grid):
        for x, column in enumerate(row):
            if grid[y][x] != True and grid[y][x] != '1': continue
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dy == 0 and dx == 0:
                        continue
                    save(x + dx, y + dy)
    return result

"""

if __name__ == '__main__':
    main()



"""

#Verificar las de x
            
"""