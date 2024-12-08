

def main():
    box =   [
              "###",
              "# #",
              "###"
            ]
    box2 =  [
              "####",
              "#* #",
              "#  #",
              "####"
            ]
    box3 =  [
              "#####",
              "#   #",
              "#  #*",
              "#####"
            ]
    box4 = [
              "#####",
              "#   #",
              "#   #",
              "#   #",
              "#####"
            ]
    print(in_box(box4))



# 5 estrellas
def in_box(box):
    gift_symbol = "*"
    not_permited = [0,len(box[0])-1]

    #Verificar bordes superiores e inferiores
    if gift_symbol in box[0] or gift_symbol in box[len(box)-1]:
        return False

    #Verify box's body
    for row in box[1:-1]:
        # Verificar si exite regalo en la row
        if gift_symbol not in row:
            continue

        #Verificar bordes
        if row.index(gift_symbol) in not_permited:
            return False
        else:
            return True
    return False


#4 estrellas
"""
def in_box(box):
    box_height = len(box)-1
    box_width = len(box[0])-1
    gift_symbol = "*"
    hash_symbol = "#"
    not_permited = [0,box_width]

    #Verificar bordes superiores e inferiores
    if gift_symbol in box[0] or gift_symbol in box[box_height]:
        return False

    #Verify box's body
    for row in box[1:-1]:
        # Verificar si exite regalo en la row
        if gift_symbol not in row:
            continue

        #Verificar bordes
        if row.index(gift_symbol) in not_permited:
            return False
        else:
            return True

    return False
"""

if __name__ == '__main__':
    main()