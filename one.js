
class demo {
    constructor(name, age) {
        this.name = name
        this.age = age
    }

    printName() {
        return console.log(this.name + this.age)
    }
}

let name = new demo("New", "Name")
name.printName();