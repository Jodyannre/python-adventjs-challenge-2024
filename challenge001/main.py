def main():
    print(prepare_gifts([3, 1, 2, 3, 4, 2, 5]))

def prepare_gifts(gifts):
    return sorted(set(gifts))

if __name__ == "__main__":
    main()
