
// class demo {
//     constructor(name, age) {
//         this.name = name
//         this.age = age
//     }

//     printName() {
//         return console.log(this.name + this.age)
//     }
// }

// let name = new demo("New", "Name")
// name.printName();


// function outerFunction(x) {
//     console.log(x);
//     return function innterFunction(y) {
//         console.log(y);
//         return x + y
//     }
// }

// const outerFunction5 = outerFunction(5)
// console.log(outerFunction5)
// console.log(outerFunction5(3));

// const shape = {
//     radius: 10,
//     diameter() {
//         return this.radius * 2;
//     },
//     perimeter: () => 2 * Math.PI * this.radius,
// };

// console.log(shape.diameter());
// console.log(shape.perimeter());

// let c = { greeting: 'Hey!' };
// let d;

// d = c;
// c.greeting = 'Hello';
// console.log(d.greeting);

// let a = 3;
// let b = new Number(3);
// let c = 3;

// console.log(a == b);
// console.log(a === b);
// console.log(b === c);

// let number = 0;

// console.log(number++);

// console.log(++number);

// console.log(number);


let number = 0

console.log(number)
console.log(number++)
console.log(++number)
console.log(number)