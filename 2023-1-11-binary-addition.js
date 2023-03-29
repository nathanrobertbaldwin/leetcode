var addBinary = function(a, b) {

    let splitA = a.split("").reverse().map(ele => parseInt(ele));
    let splitB = b.split("").reverse().map(ele => parseInt(ele));

    let diffLength = Math.abs(splitA.length - splitB.length);

    let toAddTo = (splitB.length <= splitA.length) ? splitB : splitA;

    for (let i = 0; i < diffLength; i++) {
        toAddTo.push(0)
    }

    let sum = [];

    for (let i = 0; i < splitA.length; i++) {
        sum.push(splitA[i] + splitB[i])
    }

    for (let i = 0; i < sum.length; i++) {
        if (i === sum.length - 1) {
            if (sum[i] > 1) {
                sum[i] -= 2;
                sum.push(1);
            }
        } else if (sum[i] > 1) {
            sum[i] -= 2;
            sum[i + 1] += 1;

        }
    }

    return sum.reverse().join("")
}

console.log(addBinary("11", "1"))
