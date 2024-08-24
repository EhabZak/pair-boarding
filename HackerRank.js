
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

//! 3

// function lonelyInteger(a) {
// // solution 1
// return a.reduce((unique, num) => unique ^ num, 0);

// // solution 2

// //     let b = {}

// //     for (let num of a) {
// //         if (num in b) {
// //             b[num] += 1
// //         } else {
// //             b[num] = 1
// //         }
// //     }

// //     for (let n in b) {
// //         if (b[n] === 1) {
// //             return n
// //         }
// //     }
// }

// let str = [1, 2, 3, 4, 3, 2, 1] // output 2

// console.log(lonelyInteger(str))

// console.log(lonelyInteger(str))





//     //    let res = nestedArray.concat(num)


/*
 Given an array of integers, where all elements but one occur twice, find
 the unique element.Example= [1,2,3,4,3,2,1]
 a=The unique element is 4.Function Description Complete the lonely integer function in the editor below.
 lonely integer has the following parameter(s):• int a[n]: an array of integers. Returns
int: the element that occurs only once Input Format The first line contains a single integer, n, the
number of integers in the array. The second line contains n space-separated integers that describe the
value in a
 */

// function simpleHash(str) {
//     let hashValue = 0;

//     for (let i = 0; i < str.length; i++) {
//         hashValue += str.charCodeAt(i);
//     }

//     return hashValue;
// }

// console.log(simpleHash('addd'))

//! 4-Flipping bits

/*
input = 1
1-convert to 32 ok
Binary representation: 00000000000000000000000000000001 ok
2-Flipping the bits: 11111111111111111111111111111110 ok
3-Decimal value of the flipped bits: 4294967294
*/
/*
You will be given a list of 32 bit unsigned integers. Flip all the bits ( and ) and return the result as an unsigned integer.

Example

. We're working with 32 bits, so:



Return .

Function Description

Complete the flippingBits function in the editor below.

flippingBits has the following parameter(s):

int n: an integer
Returns

int: the unsigned decimal integer result
Input Format

The first line of the input contains , the number of queries.
Each of the next  lines contain an integer, , to process.

Constraints



Sample Input

3
2147483647
1
0
Sample Output

2147483648
4294967294
4294967295
Explanation

Take 1 for example, as unsigned 32-bits is
00000000000000000000000000000001 and doing the
flipping we get 11111111111111111111111111111110
which in turn is 4294967294.

*/



    // function flippingBits(n) {
    //     // Convert the number to a binary string
    //     let binaryStr = n.toString(2);

    //     // Pad the binary string with leading zeros to ensure it's 32 bits
    //     let paddedBinaryStr = binaryStr.padStart(32, '0');

    //     // Initialize an empty string to store the flipped bits
    //     let flippedBinaryStr = '';

    //     // Iterate over each bit in the padded binary string
    //     for (let bit of paddedBinaryStr) {
    //         // Flip the bit: if '0' then '1', if '1' then '0'
    //         flippedBinaryStr += bit === '0' ? '1' : '0';
    //     }

    //     // Convert the flipped binary string back to a decimal number
    //     let result = parseInt(flippedBinaryStr, 2);

    //     return result;
    // }

    // // OR a better solution
    // function flippingBits(n) {
    //     // Flip the bits using the bitwise NOT operator (~)
    //     // and convert the result to an unsigned 32-bit integer using >>> 0
    //     return (~n) >>> 0;
    // }

    // // Example usage with sample input

    // Example usage with sample input
    // console.log(flippingBits(2147483647)); // Output: 2147483648
    // console.log(flippingBits(1));          // Output: 4294967294
    // console.log(flippingBits(0));          // Output: 4294967295

    //!  5-diagonal differences

    /*
    Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

Function description

Complete the  function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers
Return

int: the absolute diagonal difference
Input Format

The first line contains a single integer, , the number of rows and columns in the square matrix .
Each of the next  lines describes a row, , and consists of  space-separated integers .

Constraints

Output Format

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

Sample Input

3
11 2 4
4 5 6
10 8 -12
Sample Output

15
Explanation

The primary diagonal is:

11
   5
     -12
Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:

     4
   5
10
Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15

Note: |x| is the absolute value of x
    */

// function diagonalDifference(arr) {
//   let sum1 = 0
//   let sum2 = 0

//   // Solution 1
//    arr.forEach((list,i)=> {
//       sum1 += list[i]
//       sum2 += list[arr.length -1 -i]

//   } )

// let result1 = Math.abs(sum1-sum2)
//   return result1

//   // Solution 2

//   // for (let i = 0 ; i < arr.length ; i++){


//   //     sum1 += arr[i][i]
//   //     sum2 += arr[i][arr.length -1 -i]
//   // }

//   // let result1 = Math.abs(sum1-sum2)
//   // return result1

// }


// let arr1 = [
//   // [3],
//   [11, 2, 4],
//   [4 ,5 ,6],
//   [10, 8, -12]
// ]
// console.log(diagonalDifference(arr1))


//! 6- Counting sort
/*
Comparison Sorting
Quicksort usually has a running time of n x log(n) , but is there an
algorithm that can sort even faster? In general, this is not possible.
Most sorting algorithms are comparison sorts, i.e. they sort a list
just by comparing the elements to one another. A comparison sort
algorithm cannot beat  (worst-case) running time, since  represents
the minimum number of comparisons needed to know where to place each
element. For more details, you can see these notes (PDF).

Alternative Sorting
Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose index range covers the entire range of values in your array to sort. Each time a value occurs in the original array, you increment the counter at that index. At the end, run through your counting array, printing the value of each non-zero valued index that number of times.

Example

All of the values are in the range , so create an array of zeros, . The results of each iteration follow:

i	arr[i]	result
0	1	[0, 1, 0, 0]
1	1	[0, 2, 0, 0]
2	3	[0, 2, 0, 1]
3	2	[0, 2, 1, 1]
4	1	[0, 3, 1, 1]
The frequency array is . These values can be used to create the sorted array as well: .


*/
