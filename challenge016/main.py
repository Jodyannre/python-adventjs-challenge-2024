from functools import reduce

def main():
    remove_snow("zxxzoz")
    remove_snow("abcdd")
    remove_snow("zzz")

# 5 *****
def remove_snow(s: str) -> str:
    return reduce(lambda x, y: x[:-1] if x[-1:] == y else x+y, s)

if __name__ == '__main__':
    main()