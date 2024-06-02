
//! 1-Time conversion  Change time PM/AM

// function timeConversion(s) {
// Write your code here

//     let period = s.slice(-2)
//     console.log(period)


//     let [hour, min, sec] = s.slice(0, -2).split(":")

//     if (period === 'PM') {

//         if (hour !== '12') {
//             hour = String(Number(hour) + 12)
//         }
//     } else {
//         if (hour === "12") {
//             hour = '00'
//         }
//     }

//     return `${hour}:${min}:${sec}`

// }

// let input = "07:05:45PM"
// let input = "12:05:45AM"

// let input = "07:05:45AM"
// 19:05:45


// console.log(timeConversion(input))








//! #! 2-Sparse Arrays

// function matchingStrings(strings, queries) {
//     // Write your code here
//     let res = []
//     let count = 0
//     for (let query of queries) {

//         for (let string of strings) {
//             if (string === query) {
//                 count += 1
//             }
//         }
//         res.push(count)
//         count = 0
//     }

//     return res

// }

// let strings = ["aba"
//     , "baba"
//     , "aba"
//     , "xzxb"]

// let queries = [
//     "aba"
//     , "xzxb"
//     , "ab"
// ]

// // let strings = [
// // 'def',
// // 'de',
// // 'fgh'
// // ]
// // let queries = [

// //     'de',
// //     'lmn',
// //     'fgh'

// // ]

// console.log(matchingStrings(strings, queries))

//!

function lonelyInteger(a) {
// solution 1
return a.reduce((unique, num) => unique ^ num, 0);

// solution 2

//     let b = {}

//     for (let num of a) {
//         if (num in b) {
//             b[num] += 1
//         } else {
//             b[num] = 1
//         }
//     }

//     for (let n in b) {
//         if (b[n] === 1) {
//             return n
//         }
//     }
}

let str = [1, 2, 3, 4, 3, 2, 1] // output 2

console.log(lonelyInteger(str))

// console.log(lonelyInteger(str))





//     //    let res = nestedArray.concat(num)


/*
 Given an array of integers, where all elements but one occur twice, find
 the unique element.Example= [1,2,3,4,3,2,1]
 a=The unique element is 4.Function DescriptionComplete the lonely integer function in the editor below.
 */
