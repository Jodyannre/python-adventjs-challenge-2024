


def main():
    dataSet = [
    { "name": 'Alice', "city": 'London' },
    { "name": 'Bob', "city": 'Paris' },
    { "name": 'Charlie', "city": 'New York' }
    ]

    dataSet2 = [
        {"gift": 'Doll', "quantity": 10},
        {"gift": 'Book', "quantity": 5},
        {"gift": 'Music CD', "quantity": 1}
    ]

    dataSet = [
        { "name": 'Alice', "city": 'London' }
    ]

    dataSet = [
      { "game": 'indianajones', "subtitle": 'the game'},
    { "game": 'pokemonblue', "subtitle": ''}
    ]

    print(draw_table(dataSet))





def draw_table(data: list[dict[str, str | int]]) -> str:
    dataSet = data
    keys = list(dataSet[0].keys())
    max_width = []
    values = []
    result = ""
    for d in keys:
        max_width.append([len(d)])
        values.append([])

    for data in dataSet:
        for key in range(0, len(keys)):
            acc_max_value = max_width[key].pop()
            acc_data = data[keys[key]]
            max_width[key].append(max(acc_max_value, len(str(acc_data))))
            values[key].append(acc_data)

    # Pintar cabeceras
    for key in range(0, len(keys)):
        result += f"+{(max_width[key][0] + 2) * '-'}"
    result += "+\n"

    for key in range(0, len(keys)):
        result += "|" + " " + keys[key].capitalize() + " " * (max_width[key][0] - len(keys[key])) + " "
    result += "|\n"

    for key in range(0, len(keys)):
        result += f"+{(max_width[key][0] + 2) * '-'}"
    result += "+\n"

    for j in range(0, len(dataSet)):
        for i in range(len(keys)):
            max_w = max_width[i][0]
            acc = values[i][j]
            result += "|" + " " + str(acc) + " " * (max_w - len(str(acc))) + " "

        result += "|\n"

    # Pintar footer
    for key in range(0, len(keys)):
        result += f"+{(max_width[key][0] + 2) * '-'}"
    result += "+\n"

    return result


# First attemp

"""
def draw_table(data: list[dict[str, str | int]]) -> str:
    # Crear listas para guardar datos
    keys = list(data[0].keys())
    keys.reverse()

    def paint(index, max_length):
        acc = data[index]
        result = ""
        for key in keys:
            max_length = max(max_length, len(str(acc[key])))

        if index < len(data) - 1:
            result, max_length = paint(index + 1, max_length)

        for key in range(0, len(keys)):
            acc = data[index][keys[key]]
            result = "|" + " " + str(acc) + " " * (max_length - len(str(acc))) + " " + ("|\n" if key == 0 else "") + result

        if index == len(data) - 1:
            result += "+" + ((max_length + 2) * "-" + "+") * 2

        if index == 0:
            temp = "+" + ((max_length + 2) * "-" + "+") * 2 + "\n"
            keys.reverse()
            for key in keys:
                temp += "|" + " " + key.capitalize() + " " * (max_length - len(key)) + " "
            temp += "|\n"
            temp += "+" + ((max_length + 2) * "-" + "+") * 2 + "\n"
            result = temp + result

        return result, max_length

    return paint(0, 0)[0]
"""

if __name__ == '__main__':
    main()