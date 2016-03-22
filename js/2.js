var a = 1;
var b = 2;
var total = 0;
while (a < 4000000) {
    if (a % 2 == 0) {
        total += a;
    }
    var temp = a;
    a = b;
    b = a + temp;
}

console.log(total);