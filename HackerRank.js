
//! Time conversion  Change time PM/AM

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









function matchingStrings(strings, queries) {
    // Write your code here
    let res = []
    let count = 0
    for (let query of queries) {

        for (let string of strings) {
            if (string === query) {
                count += 1
            }
        }
        res.push(count)
        count = 0
    }

    return res

}

let strings = ["aba"
    , "baba"
    , "aba"
    , "xzxb"]

let queries = [
    "aba"
    , "xzxb"
    , "ab"
]

// let strings = [
// 'def',
// 'de',
// 'fgh'
// ]
// let queries = [

//     'de',
//     'lmn',
//     'fgh'

// ]




console.log(matchingStrings(strings, queries))
