divides = function (x, attempt) {
    return x % attempt == 0
}
var number = 600851475143;
var x = 2;
while(x <= number) {
    while(divides(number, x)) {
        number = number / x;
    }
    x += 1;
}
console.log(x - 1);