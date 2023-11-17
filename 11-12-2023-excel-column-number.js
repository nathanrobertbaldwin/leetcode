function convertToTitle(columnNumber) {

    let map = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    let res = ""

    while (columnNumber > 0) {
        let remainder = (columnNumber % 26);
        if (remainder === 0) res = "Z" + res;
        else res = map[remainder] + res;

        if (columnNumber === 26) return res;

        columnNumber = Math.floor(columnNumber / 26) - 1;
    }

    return res;

}

console.log(convertToTitle(701))