def main():
    print(distribute_weight(5))
    pass


def distribute_weight(weight: int) -> str:
    if weight <= 0: return ""
    x = weight
    result = ""
    acc_box = ""
    acc_size = None
    prev_size = None
    while x > 0:
        if x >= 10:
            x -= 10
            prev_size = acc_size
            acc_size = 9
        elif 5 <= x < 10:
            x -= 5
            prev_size = acc_size
            acc_size = 5
        elif 2 <= x < 5:
            x -= 2
            prev_size = acc_size
            acc_size = 3
        else:
            prev_size = acc_size
            x -= 1
            acc_size = 1

        if acc_size >= 5:
            acc_box += "|" + " " * acc_size + "|" + "\n"
        if not prev_size:
            acc_box += "|" + "_" * acc_size + "|"
        else:
            next = 0 if prev_size==acc_size else prev_size-(acc_size+1)
            acc_box += "|" + "_" * acc_size + "|"+ "_" * (next) + "\n"

        result = acc_box + result
        acc_box = ""

    result = " " + "_" * acc_size + " " + "\n" + result
    return result


if __name__ == '__main__':
    main()