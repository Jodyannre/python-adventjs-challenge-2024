function distributeWeight(weight) {
    if (weight <= 0) return "";
    let x = weight;
    let result = "";
    let accBox = "";
    let accSize = null;
    let prevSize = null;

    while (x > 0) {
        if (x >= 10) {
            x -= 10;
            prevSize = accSize;
            accSize = 9;
        } else if (x >= 5 && x < 10) {
            x -= 5;
            prevSize = accSize;
            accSize = 5;
        } else if (x >= 2 && x < 5) {
            x -= 2;
            prevSize = accSize;
            accSize = 3;
        } else {
            prevSize = accSize;
            x -= 1;
            accSize = 1;
        }

        if (accSize >= 5) {
            accBox += "|" + " ".repeat(accSize) + "|" + "\n";
        }
        if (prevSize === null) {
            accBox += "|" + "_".repeat(accSize) + "|";
        } else {
            const next = prevSize == accSize ? 0 : prevSize - (accSize + 1);
            accBox += "|" + "_".repeat(accSize) + "|" + "_".repeat(next) + "\n";
        }

        result = accBox + result;
        accBox = "";
    }

    result = " " + "_".repeat(accSize) + " " + "\n" + result;
    return result;
}


console.log(distributeWeight(121))