def main():
    array = [
      { "name": 'doll', "quantity": 5, "category": 'toys' },
      { "name": 'car', "quantity": 3, "category": 'toys' },
      { "name": 'ball', "quantity": 2, "category": 'sports' },
      { "name": 'car', "quantity": 2, "category": 'toys' },
      { "name": 'racket', "quantity": 4, "category": 'sports' }
    ]

    array2 = [
        {"name": 'book', "quantity": 10, "category": 'education'},
        {"name": 'book', "quantity": 5, "category": 'education'},
        {"name": 'paint', "quantity": 3, "category": 'art'}
    ]
    print(organizeInventory(array))
    print(organizeInventory(array2))


def organizeInventory(inventory):
    dictionary = {}

    for item in inventory:
        category = item['category']
        name = item['name']
        quantity = item['quantity']

        if category not in dictionary:
            dictionary[category] = {}

        dictionary[category][name] = dictionary[category].get(name,0) + quantity
    return dictionary


if __name__ == '__main__':
    main()