function minMovesToStables(reindeer: number[], stables: number[]): number {
    reindeer.sort()
    return stables.sort().reduce((acc, curr, index) => acc + Math.abs(curr - reindeer[index]), 0)
  }


  console.log(minMovesToStables([2, 6, 9], [3, 8, 5]))
  console.log(minMovesToStables([1, 1, 3], [1, 8, 4]))