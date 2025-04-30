
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


function outerFunction(x) {
    console.log(x);
    return function innterFunction(y) {
        console.log(y);
        return x + y
    }
}

const outerFunction5 = outerFunction(5)
console.log(outerFunction5)
console.log(outerFunction5(3));