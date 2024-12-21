

def main():
    tree = {
        "value": '🎁',
        "left": {
            "value": '🎄',
            "left": {
                "value": '⭐',
                "left": None,
                "right": None
            },
            "right": {
                "value": '🎅',
                "left": None,
                "right": None
            }
        },
        "right": {
            "value": '❄️',
            "left": None,
            "right": {
                "value": '🦌',
                "left": None,
                "right": None
            }
        }
    }

    print(tree_height(tree))

def tree_height(tree):
    level = 0
    if tree is None: return level
    level+=1
    return level + max(tree_height(tree["left"]),tree_height(tree["right"]))

if __name__ == '__main__':
    main()



