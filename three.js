const person = {
    name: "John",
    greet: function (message) {
        return `${message}, ${this.name}!`;
    }
};

const anotherPerson = {
    name: "Jane"
};

// call() example
const greetingCall = person.greet.call(anotherPerson, "Hello");
console.log(greetingCall); // Output: Hello, Jane!

// apply() example
const greetingApply = person.greet.apply(anotherPerson, ["Hi"]);
console.log(greetingApply); // Output: Hi, Jane!

// bind() example
const greetJane = person.greet.bind(anotherPerson);
console.log(greetJane("Greetings")); // Output: Greetings, Jane!