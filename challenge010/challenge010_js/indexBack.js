function compile (instructions) {
    
    let op_table = instructions.map((x) => x.split(" "));
    let sym_table = {};
    let [op,arg1,arg2] = ["", "", ""];
    let value = -1;

    for (let op_index = 0; op_index < op_table.length; op_index++) {
        [op,arg1,arg2] = op_table[op_index]
        value = sym_table[arg1];
        switch(op) {
            case 'MOV':
                sym_table[arg2] = isNaN(Number(arg1)) ? (value || 0) : Number(arg1);
                break;
            case 'JMP':
                if (isNaN(value) || value == 0) {
                    sym_table[arg1] = 0
                    op_index = Number(arg2) - 1;
                    if (op_index < 0) return undefined
                };
                break;
            case 'INC':
            case 'DEC':
                sym_table[arg1] = (!isNaN(value)? value : 0) + (op =='INC' ? 1 : -1)
                break;
        }
    }

    return sym_table['A'] || undefined;
}

let instructions = [
    'MOV -1 C',
    'INC C',
    'JMP C 1',
    'MOV C A',
    'INC A'
  ]

let instructions2 = [
      'MOV 5 B',
      'DEC B',
      'MOV B A',
      'INC A'
  ]

let instructions3 = [
      'INC A',
      'INC A',
      'DEC A',
      'MOV A B'
  ]

let instructions4 = [
    "MOV 3 C",
    "DEC C",
    "DEC C",
    "DEC C",
    "JMP C 3",
    "MOV C A"
]

let instructions5 = [
    'INC B',
    'INC B',
    'DEC C',
    'MOV B C'
]


console.time('compile')
console.log(compile(instructions4))
console.timeEnd('compile')


let dict = {}
