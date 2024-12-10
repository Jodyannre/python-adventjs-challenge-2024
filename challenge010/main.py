



def main():
    instructions1 = [
      'MOV -1 C',
      'INC C',
      'JMP C 1',
      'MOV C A',
      'INC A'
    ]

    instructions2 = [
        'INC A',
        'INC A',
        'DEC A',
        'MOV A B'
    ]

    instructions3 = [
        'MOV 5 B',
        'DEC B',
        'MOV B A',
        'INC A'
    ]
    print(compile(instructions2))



def compile(instructions):
    sym_table = {}
    op_index = 0
    #Obtener instrucciones
    op, arg1, arg2 = ["", "", ""]
    while op_index < len(instructions):

        instruction = instructions[op_index]

        if 'INC' in instruction or 'DEC' in instruction:
            op,arg1 = instruction.split(" ")
        else:
            op,arg1,arg2 = instruction.split(" ")

        op_index += 1

        match op:
            case 'MOV':
                try:
                    sym_table[arg2] = int(arg1)
                except:
                    sym_table[arg2] = sym_table.setdefault(arg1, 0)
            case 'JMP':
                if sym_table.setdefault(arg1, 0) == 0:
                    op_index = int(arg2)
            case 'INC':
                sym_table[arg1] = sym_table.setdefault(arg1, 0) + 1
            case 'DEC':
                sym_table[arg1] = sym_table.setdefault(arg1, 1) - 1

    return sym_table['A']



if __name__ == '__main__':
    main()