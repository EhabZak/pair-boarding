let arr = [5,6,7,8,9]

// let doubleArr = arr.forEach(function(element){
//     console.log(element * 2)
// })

// console.log(doubleArr)


const multiply = (Array) => arr.map((element)=> element *5)

function multi(Array){

    return arr.filter((element)=> element % 5 == 0 )
}
console.log(multi(arr))
// console.log(multiply(arr))
