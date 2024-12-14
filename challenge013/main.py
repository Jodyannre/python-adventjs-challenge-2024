from unittest import case


def main() :
    is_robot_back('R') # [1, 0]
    is_robot_back('RL') # true
    is_robot_back('RLUD') # true
    is_robot_back('*RU') # [2, 1]
    is_robot_back('R*U') # [1, 2]
    is_robot_back('LLL!R') # [-4, 0]
    is_robot_back('R?R') # [1, 0]
    is_robot_back('U?D') # true
    is_robot_back('R!L') # [2, 0]
    is_robot_back('U!D') # [0, 2]
    is_robot_back('R?L') # true
    is_robot_back('U?U') # [0, 1]
    is_robot_back('*U?U') # [0, 2]
    is_robot_back('U?D?U') # true????
    is_robot_back('R!U?U')





def is_robot_back(moves: str) -> bool | list[int]:
    dictionary = {
        'D':{'invert':'U','calc':[0,-1]},
        'U':{'invert':'D','calc':[0,1]},
        'L':{'invert':'R','calc':[-1,0]},
        'R':{'invert':'L','calc':[1,0]},
    }
    pos_init = [0,0]
    prev_op = None
    prev_move = None
    compute = []
    for op in moves:

        if op not in ['R','L','U','D','*','!','?']:
            return pos_init
        #Classify the type of op
        match op:
            case 'R'|'L'|'U'|'D':
                pass
            case _:
                prev_op = op
                continue

        #Find the next calc to perform
        match prev_op:
            case '*':
                compute = [x*2 for x in dictionary[op]['calc']]
                prev_move = op
            case '!':
                prev_move = dictionary[op]['invert']
                compute = dictionary[prev_move]['calc']
            case '?':
                compute = dictionary[op]['calc'] if prev_move != op else [0,0]
                prev_move = op
            case None:
                compute = dictionary[op]['calc']
                prev_move = op

        #Update variables
        prev_op = None

        #Computar
        pos_init[0] += compute[0]
        pos_init[1] += compute[1]
    print(True if pos_init == [0,0] else pos_init)
    return True if pos_init == [0,0] else pos_init


if __name__ == '__main__':
    main()