function compile (instructions) {
    let sym_table = {};
    let ins_table = instructions.map((x) => {
        let ins = x.split(" ")
        sym_table[ins[1]] = 0;
        if (ins.length > 2) sym_table[ins[2]] = 0;
        return ins
    })

    let [op,arg1,arg2] = ["", "", ""];

    for (let op_index = 0; op_index < ins_table.length; op_index++) {

        [op,arg1,arg2] = ins_table[op_index]

        switch(op) {
            case 'MOV':
                sym_table[arg2] = Number(arg1)? Number(arg1) : sym_table[arg1] 
                continue;
            case 'INC':
            case 'DEC':
                sym_table[arg1] = sym_table[arg1]  + (op =='INC' ? 1 : -1)
                continue;
            case 'JMP':
                if (sym_table[arg1] == 0) {
                    op_index = Number(arg2) - 1;
                    if (op_index < 0) return undefined
                };
                continue;
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


console.time('cadena')
console.log("MOV" == "INC")
console.timeEnd('cadena')

console.time('numero')
console.log(1 == 12)
console.timeEnd('numero')