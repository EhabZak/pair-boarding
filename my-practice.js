function diagonalDifference(arr) {
  let sum1 = 0
  let sum2 = 0

  // Solution 1
  arr.forEach((list,i)=> {
    sum1 += list[i]
    sum2 += list[arr.length -1 -i]

} )

let result1 = Math.abs(sum1-sum2)
return result1

// Solution 2

// for (let i = 0 ; i < arr.length ; i++){


//     sum1 += arr[i][i]
//     sum2 += arr[i][arr.length -1 -i]
// }

