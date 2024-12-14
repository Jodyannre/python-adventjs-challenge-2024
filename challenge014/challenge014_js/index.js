function minMovesToStables(reindeer, stables) {
    let result = 0
    reindeer.sort()

    stables.sort().forEach((element,index) => {
        result += Math.abs(element - reindeer[index])
    });

    return result
}


    console.log(minMovesToStables([2, 6, 9], [3, 8, 5]))
    console.log(minMovesToStables([1, 1, 3], [1, 8, 4]))