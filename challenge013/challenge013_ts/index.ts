/* 5 **** */

function isRobotBack(moves: string): true | [number, number] {
    const opposites = {'U': 'D','D': 'U','R': 'L','L': 'R',}
    let i = 0
    const moves_array = [...moves]
    let [x,y] = [0,0]

    const dictionary= {
        'U': (index:number)=> {
            i = index+1
            y++
            return 'U'
        },
        'D': (index:number)=> {
            i = index+1
            y--
            return 'D'
        },
        'R': (index:number)=> {
            i = index+1
            x++
            return 'R'
        },
        'L': (index:number)=> {
            i = index+1
            x-- 
            return 'L'
        },
        '!': (index:number)=> {
            moves_array[index+1] = opposites[moves_array[index+1]]
            i = index + 1
        },
        '*': (index:number)=> dictionary[moves_array[index+1]](index),
        '?': (index:number)=> {
            const res = moves_array[index+1]
            if (moves_array.indexOf(res) < index) {
                i = index+2
                return res
            }
            i = index+1
            return res
        }
    }

    while (i < moves_array.length) dictionary[moves_array[i]](i)
    if (x == 0 && y == 0) return true
    return [x,y]
}


isRobotBack('R')     // [1, 0]
isRobotBack('RL')    // true
isRobotBack('RLUD')  // true
isRobotBack('*RU')   // [2, 1]
isRobotBack('R*U')   // [1, 2]
isRobotBack('LLL!R') // [-4, 0]
isRobotBack('R?R')   // [1, 0]
isRobotBack('U?D')   // true
isRobotBack('R!L')   // [2,0]
isRobotBack('U!D')   // [0,2]
isRobotBack('R?L')   // true
isRobotBack('U?U')   // [0,1]
isRobotBack('*U?U')  // [0,2]
isRobotBack('U?D?U') // true






/* FUNCIONA - 2 **

function isRobotBack(moves: string): true | [number, number] {
    const opposites = {
        'U': 'D',
        'D': 'U',
        'R': 'L',
        'L': 'R',
    }
    let i = 0
    const moves_array = [...moves]
    let [x,y] = [0,0]

    const operations = {
        'U': ()=>  y++,
        'D': ()=>  y--,
        'R': ()=>  x++,
        'L': ()=>  x--
    }

    const dictionary= {
        'U': (index:number)=> {
            i = index+1
            return 'U'
        },
        'D': (index:number)=> {
            i = index+1
            return 'D'
        },
        'R': (index:number)=> {
            i = index+1
            return 'R'
        },
        'L': (index:number)=> {
            i = index+1
            return 'L'
        },
        '!': (index:number)=> {
            moves_array[index] = opposites[dictionary[moves_array[index+1]](index+1)]
            moves_array.splice(index+1, 1)
            i = index + 1
            return moves_array[index]
        },
        '*': (index:number)=> {
            moves_array[index] = dictionary[moves_array[index+1]](index+1)
            return moves_array[index]
        },
        '?': (index:number)=> {
            const res = dictionary[moves_array[index+1]](index+1)
            if (moves_array.indexOf(res) < index) {
                moves_array.splice(index, 2)
                i = index
                return moves_array[index]
            }
            moves_array.splice(index, 1)
            i = index
            return res
        }
    }

    while (i < moves_array.length) {
        dictionary[moves_array[i]](i)
    }

    i = 0

    for (i; i < moves_array.length; i++) {
        operations[moves_array[i]]()
    }
    
    if (x == 0 && y == 0) {
        return true
    }
    return [x,y]
}

*/


/* Funciona - 1 *

function isRobotBack(moves: string): true | [number, number] {

    type Dictionary = {
        [key in 'U' | 'D' | 'R' | 'L' | '*'| '!'|'?']: (mov?: string) => void;
    };

    const opposites = {
        'U': 'D',
        'D': 'U',
        'R': 'L',
        'L': 'R',
    }

    const op_done = new Set<string>()
    let i = 0
    const moves_array = [...moves]
    let [x,y] = [0,0]

    const dictionary:Dictionary= {
        'U': ()=> {
            return 'U'
        },
        'D': ()=> {
            return 'D'
        },
        'R': ()=> {
            return 'R'
        },
        'L': ()=> {
            return 'L'
        },
        '*': (index:number)=> {
            const next = moves_array[index+1]
            const res = dictionary[next](index+1)
            dictionary[res](index+1, next)
            return res
        },
        '!': (index:number)=> {
            const next = moves_array[index+1]
            const res = dictionary[next](index+1)
            const opposite = opposites[res]

            return opposite
        },
        '?': (index:number)=> {
            const res =  dictionary[moves_array[index+1]](index+1)

            if (moves_array.slice(0,index+1).includes(res)) {
                const opposite = opposites[res]
                dictionary[opposite](index+1)
                return opposite
            }

            i = index+2
            return res 
        },
    }

    while (i < moves_array.length) {
        let char = moves_array[i]
        dictionary[char](i)
    }

    
    if (x == 0 && y == 0) {
        console.log(true)
        return true
    }
    console.log([x,y])
    return [x,y]
}
    
*/







/*
function isRobotBack(moves: string): true | [number, number] {

    type Dictionary = {
        [key in 'U' | 'D' | 'R' | 'L' | '*'| '!'|'?']: (mov?: string) => void;
    };

    const opposites = {
        'U': 'D',
        'D': 'U',
        'R': 'L',
        'L': 'R',
    }

    const validOperations = new Set<Operations>(['*', '!', '?']);

    const op_done = new Set<string>()
    let op_stack = []
    let pending_op = []

    const moves_array = [...moves]
    let [x,y] = [0,0]
    const dictionary:Dictionary= {
        'U': ()=> {
            y++
            op_done.add('U')
        },
        'D': ()=> {
            y--
            op_done.add('D')
        },
        'R': ()=> {
            x++
            op_done.add('R')
        },
        'L': ()=> {
            x--
            op_done.add('L')
        },
        '*': (mov: string)=> {
            pending_op.push(mov)
            dictionary[mov]()
            return mov
        },
        '!': (mov: string)=> {
            pending_op.push(opposites[mov])
            return mov
        },
        '?': (mov: string)=> {
            if (op_done.has(mov)) {
                pending_op = []
                return mov
            }
            dictionary[mov]()
            return mov 
        },
    }

    for (let i=0; i < moves.length; i++) {
        let char = moves_array[i]

        if (validOperations.has(char)) {
            op_stack.push(char)
            continue
        }

        if (op_stack.length <= 0) {
            dictionary[char]()
            continue
        }

        while (op_stack.length > 0) {
            const op = op_stack.pop()
            char = dictionary[op](char)
            
        }

        if (pending_op) {
            while (pending_op.length > 0) {
                dictionary[pending_op.pop()]()
            }
        }
    }


    if (x == 0 && y == 0) {
        return true
    }

    return [x,y]
}
*/



