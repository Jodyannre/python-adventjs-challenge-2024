def main():
    print(execute('+++')) # 3
    print(execute('+--')) # -1
    print(execute('>+++[-]')) # 0
    print(execute('>>>+{++}')) # 3
    print(execute('+{[-]+}+')) # 2
    print(execute('{+}{+}{+}')) # 0
    print(execute('------[+]++')) # 2
    print(execute('-[++{-}]+{++++}')) # 5

def execute(code: str) -> int:
    value = 0
    loop_init = -1
    i = 0
    while i < len(code):
        instruction = code[i]
        match instruction:
            case ']':
                if value != 0:
                    i = loop_init
            case '[':
                if value == 0:
                    i = code.find(']', i)
                else:
                    loop_init = i
            case '{':
                if value == 0:
                    i = code.find('}',i)
            case '+':
                value += 1
            case '-':
                value -= 1
        i += 1
    return value

if __name__ == '__main__':
    main()