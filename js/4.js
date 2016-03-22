reverse = function (s) {
    return s.toString().split("").reverse().join("");
}

ispal = function (x) {
    return x.toString() === reverse(x)
}
var best = 0;
for (var x = 100; x < 1000; x++) {
    for (var y = 100; y < 1000; y++) {
        var product = x * y;
        if (product < best) {
            continue;
        }
        if (ispal(product)) {
            best = product;
        }
    }
}
console.log(best);