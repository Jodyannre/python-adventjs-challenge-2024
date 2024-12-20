def main():

    received = ['puzzle', 'car', 'doll', 'car']
    expected = ['car', 'puzzle', 'doll', 'ball']

    received = ['book', 'train', 'kite', 'train']
    expected = ['train', 'book', 'kite', 'ball', 'kite']

    received = ['bear', 'bear', 'car']
    expected = ['bear', 'car', 'puzzle', 'bear', 'car', 'car']

    received = ['bear', 'bear', 'car']
    expected = ['car', 'bear', 'bear']
    fix_gift_list(received, expected)

def fix_gift_list(received: list[str], expected: list[str]) -> dict[str,dict[str,int]]:
    i = len(received)
    j = len(expected)
    max_size = i if i > j else j
    result = { "missing" : {},"extra" : {} }
    founded = {}

    for k in range(0, max_size):
        rec =  -1 if k >= i else received[k]
        exp =  -1 if k >= j else expected[k]
        founded[rec] = founded.get(rec, 0) + 1
        founded[exp] = founded.get(exp, 0) - 1

    for key, value in founded.items():
        if key == -1: continue
        if value > 0: result["extra"][key] = value
        if value < 0: result["missing"][key] = value*-1

    return result

if __name__ == '__main__':
    main()