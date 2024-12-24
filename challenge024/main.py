


def main():
    tree1 = {
        "value": '🎄',
        "left": {"value": '⭐'},
        "right": {"value": '🎅'}
    }

    tree2 = {
        "value": '🎄',
        "left": {"value": '🎅'},
        "right": {"value": '⭐'}
    }

    tree3 = {
        "value": '🎄',
        "left": {"value": '🎅'},
        "right": {"value": '🎁'}
    }

    tree4 = {
        "value": '🎄',
        "left": {"value": '⭐'},
        "right": {"value": '🎅'}
    }

    tree5 = {
        "value": '🎄',
        "left": {"value": '⭐', "left":{"value":'🎅'},"right":{"value":'⭐'}},
        "right": {"value": '🎅',"left":{"value":'⭐'},"right":{"value":'🎅'}}
    }

    tree6 = {
        "value": '🎄',
        "right": {"value": '⭐',"left":{"value":'⭐'},"right":{"value":'🎅'}},
        "left": {"value": '🎅',"left":{"value":'🎅'},"right":{"value":'⭐'}}
    }

    print(is_trees_synchronized(tree1, tree2))
    print(is_trees_synchronized(tree1, tree3))
    print(is_trees_synchronized(tree1, tree4))
    print(is_trees_synchronized(tree5, tree6))


def is_trees_synchronized(tree1, tree2):
    def in_order(node_left,node_right):
        #Verificar si existen mas nodos hijos
        if "left" in node_left and "right" in node_right:
            if not in_order(node_left["left"], node_right["right"]):
                return False
        if "right" in node_left and "left" in node_right:
            if not in_order(node_left["right"], node_right["left"]):
                return False

        if node_left["value"] != node_right["value"]:
            return False
        else:
            return True

    if in_order(tree1, tree2):
        return [True,tree1["value"]]

    return [False, tree1["value"]]


if __name__ == '__main__':
    main()