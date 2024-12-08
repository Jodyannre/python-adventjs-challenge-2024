
def main():
    print(create_xmas_tree(15,"*"))

#Mejorada, 2da versión

def create_xmas_tree(height, ornament):
    max_width = height*2 - 1
    hashtag = "#"
    result = []
    #Adding ornament
    for i in range(1,height+1):
        level = i*2-1
        space = int((max_width-level)/2)*"_"
        result.append(f'{space}{ornament*level}{space}')

    #Creating trunk
    trunk_position = int(max_width/2)*"_"
    trunk = f"{trunk_position}{hashtag}{trunk_position}"

    #Adding trunk
    result.append(trunk)
    result.append(trunk)

    return "\n".join(result)



if __name__ == "__main__":
    main()


"""
#Enviada

def create_xmas_tree(height, ornament):
    max_width = height*2 - 1
    result = ""
    #Adding ornament
    for i in range(1,height+1):
        level = i*2-1
        space = int((max_width-level)/2)
        result += "_"*space + ornament*level + "_"*space + "\n"
    #Creating trunk
    trunk_position = int(max_width/2)
    hashtag = "#"
    trunk = "_"*trunk_position + hashtag + "_"*trunk_position
    #Adding trunk
    result += trunk + "\n" + trunk

    return result
"""