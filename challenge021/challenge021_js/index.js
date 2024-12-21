

const test = treeHeight({
    value: '🎁',
    left: {
      value: '🎄',
      left: {
        value: '⭐',
        left: null,
        right: null
      },
      right: null
    },
    right: {
      value: '❄️',
      left: null,
      right: null
    }
  })


function treeHeight(tree) {
    let level = 0
    if (tree == null) return level;
    level++
    return  level + Math.max(treeHeight(tree.left), treeHeight(tree.right))
}

console.log(test) // 3