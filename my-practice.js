
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

    if (arr.length <=1) return arr

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
console.log(quickSort(arr1))

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



*/
