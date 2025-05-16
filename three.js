// call, apply, and bind are JavaScript methods that allow for the manipulation of the this context within a function. They are essential for controlling how functions are executed and how they interact with objects.
// call():
// Invokes a function directly, setting the this context to the object provided as the first argument, with subsequent arguments passed individually.
// apply():
// Similar to call(), but accepts arguments as an array. It invokes the function immediately with the specified this value and the array of arguments.
// bind():
// Creates a new function with the this context permanently bound to the provided object. It does not execute the function immediately but returns a new function that can be called later.

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