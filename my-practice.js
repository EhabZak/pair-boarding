




function diagonalDifference(arr) {
    let sum1 = 0
    let sum2 = 0

    // Solution 1
    arr.forEach((list,i)=> {
        sum1 += list[i]
        sum2 += list[arr.length -1 -i]

