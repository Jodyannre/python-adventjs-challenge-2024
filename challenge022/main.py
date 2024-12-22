#Y de nuevo vuelve a fallar en la página
def main():
    print(generate_gift_sets(['car', 'doll']))

def generate_gift_sets(gifts):
    result = []
    level = len(gifts) + 1

    def add_to_array(arr):
        for elm in arr:
            if isinstance(elm, str):
                result.append([elm])
            else:
                result.extend([elm])

    def recorrer(arr, level, acc):
        if level == 1:
            return arr[acc:]
        else:
            return [
                [y] + x if isinstance(x, list) else [y, x]
                for y in recorrer(arr, 1, acc)
                for x in recorrer(arr, level - 1, arr.index(y) + 1)
            ]

    #Ejecutar
    for i in range(1, level):
        temp = recorrer(gifts, i, 0)
        add_to_array(temp)
    return result


if __name__ == '__main__':
    main()