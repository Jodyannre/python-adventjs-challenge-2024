
def main():
    shoes = [
        {"type": 'I', "size": 38},
        {"type": 'R', "size": 38},
        {"type": 'R', "size": 42},
        {"type": 'I', "size": 41},
        {"type": 'I', "size": 42}
    ]

    shoes2 = [
        {"type": 'I', "size": 38},
        {"type": 'R', "size": 38},
        {"type": 'I', "size": 38},
        {"type": 'I', "size": 38},
        {"type": 'R', "size": 38}
    ]

    shoes3 = [
        {"type": 'I', "size": 38},
        {"type": 'R', "size": 36},
        {"type": 'R', "size": 42},
        {"type": 'I', "size": 41},
        {"type": 'I', "size": 43}
    ]

    print(organizeShoes(shoes2))


def organizeShoes(shoes):
    shoes_map = {}
    result = []

    for shoe in shoes:

        new_size = shoe['size']
        new_value = str(new_size) + shoe["type"]

        if new_size in shoes_map:
            size_array = shoes_map[new_size]

            if not size_array:
                size_array.append(new_value)
                continue

            if new_value not in size_array:
                size_array.pop()
                result.append(new_size)
                continue

            size_array.append(new_value)
        else:
            shoes_map[new_size] = [new_value]
    return result

if __name__ == "__main__":
    main()