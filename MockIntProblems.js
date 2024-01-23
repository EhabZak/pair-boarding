//! first Mock interview Problem from hackerRank ✅

/*
You are given an integer array prices representing the prices of various chocolates
 in a store. You are also given a single integer money, which represents
your initial amount of money.

You must buy exactly two chocolates in such a way that you still
have some non-negative leftover money. You would like to minimize the sum
of the prices of the two chocolates you buy.

Return the amount of money you will have leftover after buying the
two chocolates. If there is no way for you to buy two chocolates
without ending up in debt, return money. Note that the leftover
must be non-negative.



Input: prices = [1,3,2], money = 4
Output: 1

Input: prices = [4,2,3,71], money = 3
Output: 3
*/
// create a function that takes in an array and an value
// iterate over the array to find if any amount add up to a value less the the money value using regular loop with a nested loop
// if an amount is found which is less than the money amount then we deduct that from the money and return the remainder
// if no amount was found less than the money value we return the money value

//! my solution ✅
function addItems(arr, money) {

    let array = [] // [0, 1]
    for (let i = 0; i < arr.length; i++) {
        let val1 = arr[i] // 1 , 3
        for (j = i + 1; j < arr.length; j++) {
            let val2 = arr[j] //3 //2
            if (val1 + val2 <= money) { //4 //4
                let sum
                sum = money - (val1 + val2)
                array.push(sum)
            }
        }
    }
    if (array.length) {
        return Math.max(...array)
    } else {
        return money
    }
}
// [56,7,13,435,2], money = 1250

//! Danny solution ✅
function addItems2(arr, money) {
    let array = arr.sort((a, b) => a - b)
    if (array[0] + array[1] <= money) {
        let value = money - (array[0] + array[1])
        return value
    } else {
        return money
    }

}

//! Danny solution 2 ✅

function addItems3(arr, money) {
    if (arr.length < 2) return money
    // [56,7,13,435,Infinity]
    const minPrice = Math.min(...arr)
    const minIdx = arr.indexOf(minPrice)
    arr[minIdx] = Infinity
    const min2 = Math.min(...arr)

// I added this part
    let minTotal = minPrice + min2
    result = money - minTotal
    if (result < 0) return money
    else return result

}

// let prices = [56, 7, 13, 435, 2] // 1241
// let money = 1250
let prices = [4,2,3,71] // 3
let  money = 3

console.log(addItems(prices, money))
console.log(addItems2(prices, money))
console.log(addItems3(prices, money))


//! 2- 2nd Mock interview Problem from hackerRank ✅ //////////////////////////////////////////////
// function Roman(string) {
//     let Values = string.split()
//     let Arr = [] // [1,1,1]

// let Numbers = {
//     "I" : 1,
//     "V" : 5,
//     "X" : 10,
//     "L":  50,
//     "C" : 100,
//     "D" : 500,
//     "M" : 1000
// }

// for (let char in Values) {
//     Number[char]. push(Arr)
// }


// }
// this question should take 5 min to understand and do by myself but it took ??? one day??
//let s1 = "LVIII"
// var romanToInt = function(s) {
//     let total = 0
//     const convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
//     for (let i = 0; i < s.length; i++) {
//         total += convert[s[i]] // results in 2216

//         // console.log('convert[s[i]]===>', convert[s[i]])
//         // console.log('s[i]', s[i])
//     }

//     for (let i = 0; i < s.length-1; i++) {
//         if (convert[s[i]] < convert[s[i+1]]) {
//             total -=  2 * convert[s[i]]
//             // we subtract twice because we added it so we need
//             //to remove the addition then we subtract the number again to make it less
//             //like to 1100 - 100 then it will 1000 then we subtract again to make it 900
//             // console.log('total =', total)
//         }
//     }
//     return total
// };


// let s = "III"
// //Output: 3

// let s1 = "LVIII"
// //Output: 58

// let s2 = "MCMXCIV"
// //Output: 1994

// console.log(romanToInt(s2))
