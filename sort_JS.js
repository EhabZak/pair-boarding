
// function mergeSort(arr){

//     if (arr.length <= 1) return arr;

//     const mid = Math.floor(arr.length/2)
//     const leftHalf = arr.slice(0, mid);
//     const rightHalf = arr.slice(mid);


//     const leftSort= mergeSort(leftHalf)
//     const rightSort = mergeSort(rightHalf)

//     return merge(leftSort,rightSort)
// }

// function merge(arrA, arrB){

//     const res = []

//     let idxA = 0
//     let idxB = 0

//     while (idxA < arrA.length && idxB < arrB.length){

//         if (arrA[idxA] <= arrB[idxB]){
//             res.push(arrA[idxA])
//             console.log( 'idxA =========' ,  idxA)
//             idxA ++
//             console.log( 'idxA +++++++++++++++' ,  idxA)
//         }else{
//             res.push(arrB[idxB])
//             idxB ++
//         }
//     }

//     return [...res, ...arrA.slice(idxA), ...arrB.slice(idxB)]
// }

// const arr = [7,6,5,2,3,1,4]

// console.log(mergeSort(arr) )
