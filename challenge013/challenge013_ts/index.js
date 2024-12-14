var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
function isRobotBack(moves) {
    var _a, _b, _c, _d, _e;
    var dictionary = new Map([
        ["D", { 'invert': 'U', 'calc': [0, -1] }],
        ["U", { 'invert': 'D', 'calc': [0, 1] }],
        ["L", { 'invert': 'R', 'calc': [-1, 0] }],
        ["R", { 'invert': 'L', 'calc': [1, 0] }],
    ]);
    var pos_init = [0, 0];
    var prev_op = undefined;
    var prev_move = undefined;
    var compute = [];
    var char = '';
    var chars = __spreadArray([], moves, true);
    for (var index = 0; index < chars.length; index++) {
        char = chars[index];
        if (char in ['R', 'L', 'U', 'D', '*', '!', '?']) {
            return pos_init;
        }
        //Classify the type of op
        switch (char) {
            case 'R':
            case 'L':
            case 'U':
            case 'D': {
                break;
            }
            default: {
                prev_op = char;
                continue;
            }
        }
        //Find the next calc to perform
        switch (prev_op) {
            case '*': {
                compute = (_a = dictionary.get(char)) === null || _a === void 0 ? void 0 : _a.calc.map(function (x) { return x * 2; });
                prev_move = char;
            }
            case '!': {
                prev_move = (_b = dictionary.get(char)) === null || _b === void 0 ? void 0 : _b.invert;
                compute = (_c = dictionary.get(prev_move || "")) === null || _c === void 0 ? void 0 : _c.calc;
            }
            case "?": {
                compute = prev_move != char ? (_d = dictionary.get(char)) === null || _d === void 0 ? void 0 : _d.calc : [0, 0];
                prev_move = char;
            }
            case undefined: {
                compute = (_e = dictionary.get(char)) === null || _e === void 0 ? void 0 : _e.calc;
                prev_move = char;
            }
        }
        //Update variables
        prev_op = undefined;
        //Compuet
        pos_init[0] += compute ? compute[0] : 0;
        pos_init[1] += compute ? compute[1] : 0;
    }
    if (pos_init[0] == 0 && pos_init[1] == 0) {
        console.log(true);
        return true;
    }
    else {
        console.log(pos_init);
        return pos_init;
    }
}
isRobotBack('*RU'); // [2, 1]
