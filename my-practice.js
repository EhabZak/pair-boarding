
// quickSort = (arr) =>{

//     if (arr.length <= 1) return arr
//     let pivot = arr[0]

//     let left = []
//     let right = []

//     for (let i = 1; i< arr.length; i++){

//         if (arr[i]< pivot){
//             left.push(arr[i])
//         }
//         else{
//             right.push(arr[i])
//         }
//     }

//     let leftSort = quickSort(left)

//     let rightSort = quickSort(right)

//     return [...leftSort,pivot, ...rightSort]

// }

// let arr1 = [5,6,2,4,7,8,9,3]
// console.log(quickSort(arr1))

quickSort = (arr) => {

    if (arr.length <= 1) return arr

    let chosenOne = arr[0]

    let left = []
    let right = []

    for (let i = 1; i < arr.length; i++) {
        if (arr[i] < chosenOne) {
            left.push(arr[i])
        } else {
            right.push(arr[i])

        }
    }

    let leftSide = quickSort(left)
    let rightSide = quickSort(right)

    return [...leftSide, chosenOne, ...rightSide]

}

let arr1 = [5, 6, 2, 4, 7, 8, 9, 3]
// console.log(quickSort(arr1))

/*

Comparison Sorting
Quicksort usually has a running time of , but is there an algorithm that can sort even faster? In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. A comparison sort algorithm cannot beat  (worst-case) running time, since  represents the minimum number of comparisons needed to know where to place each element. For more details, you can see these notes (PDF).

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

Note
For this exercise, always return a frequency array with 100 elements. The example above shows only the first 4 elements, the remainder being zeros.


Challenge
Given a list of integers, count and return the number of times each value appears as an array of integers.

Function Description

Complete the countingSort function in the editor below.

countingSort has the following parameter(s):


arr[n]: an array of integers
Returns

int[100]: a frequency array
Input Format


The first line contains an integer , the number of items in .
Each of the next  lines contains an integer  where .

Constraints

Sample Input

100
63 25 73 1 98 73 56 84 86 57 16 83 8 25 81 56 9 53 98 67 99 12 83 89 80 91 39 86 76 85 74 39 25 90 59 10 94 32 44 3 89 30 27 79 46 96 27 32 18 21 92 69 81 40 40 34 68 78 24 87 42 69 23 41 78 22 6 90 99 89 50 30 20 1 43 3 70 95 33 46 44 9 69 48 33 60 65 16 82 67 61 32 21 79 75 75 13 87 70 33
Sample Output

0 2 0 2 0 0 1 0 1 2 1 0 1 1 0 0 2 0 1 0 1 2 1 1 1 3 0 2 0 0 2 0 3 3 1 0 0 0 0 2 2 1 1 1 2 0 2 0 1 0 1 0 0 1 0 0 2 1 0 1 1 1 0 1 0 1 0 2 1 3 2 0 0 2 1 2 1 0 2 2 1 2 1 2 1 1 2 2 0 3 2 1 1 0 1 1 1 0 2 2
Explanation

Each of the resulting values  represents the number of times  appeared in .


*/
quickSort = (arr) => {
    // create a variable for left and right create a new array
    //! you keep forgetting the BASECASE over and over
    // chose the first number then sort the numbers higher or lower
    // then recursion to sort the numbers then add all the arrays together
if (arr.length <=1) return arr //! you keep fuckeeeeeeeeeeeeeeeeeeen forgetting this line
    let left = []
    let right = []
    let num = arr[0]
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] > num) {
            right.push(arr[i])
        } else { left.push(arr[i]) }

    }

    let leftSide1 = quickSort(left)
    let rightSide1 = quickSort(right)

   
