// /*
// Implement the “transform” function below that converts any string to the string of the following format:
// a quantity of a specific character + the character itself … a quantity of another character + another character itself …
// For example, if we pass “aaabbcccccda”-string, we should get “4a2b5c1d”
// */
// function transform(s) {
//     var myStringArray = [];
//     // place your code here
//     for (let i = 0; i < s.length; i++) {
//         myStringArray.push(s[i]);
//     }


//     for (let j = 0; j < myStringArray.length; j++) {
//         let count = 0;
//         const updated = myStringArray.map((value, index) => {
//             if (value == myStringArray[j]) {
//                 count = count + 1;

//                 return { key: myStringArray[j], count: count }
//             }
//         })

//         return updated
//     }
//     console.log("happy=>", myStringArray);

// }


// const data = transform('aaabbcccccda'); // 4a2b5c1d
// // console.log(transform('@@@qq@w')); // 4@2q1w

// console.log("data=>", data);


function demo() {
    console.log(a)
    var a = 10
    console.log(a)
}

var a = 20
demo()
console.log(a)