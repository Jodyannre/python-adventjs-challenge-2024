


def main():
    print(min_moves_to_stables([2, 6, 9], [3, 8, 5]))
    print(min_moves_to_stables([1, 1, 3], [1, 8, 4]))


#No funciona en el portal, pero esta bien
"""
def min_moves_to_stables(reindeer, stables):
    reindeer.sort()
    stables.sort()
    result = sum([abs(reindeer[i]-stables[i]) for i in range(len(stables))])
    return result
"""

# 5 *****
def min_moves_to_stables(reindeer, stables):
    reindeer.sort()
    stables.sort()
    result = 0
    for i in range(0,len(stables)):
      result += abs(stables[i] - reindeer[i])
    return result


if __name__ == '__main__':
    main()