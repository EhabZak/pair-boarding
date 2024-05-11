// let num = [0, 1, 0, 3, 12]

// function check(numbers) {

//     for (let i in numbers) {

//         number = numbers[i]
//         if (number == 0) {

//             let num1 = numbers.splice(i, 1)
//             console.log(num1)
//             numbers.push(number)
//         }

//     }

//     console.log(numbers)

// }

// check(num) //[ 1, 3, 12, 0, 0 ]


reverse = (Name) =>{
    let Name2 =''

    for (let i = Name.length-1; i >= 0; i--) {

        Name2 += Name[i]

    }
    return Name2
}

// console.log(reverse('zak'))



/*
Define a function fizzBuzz(max) that takes a number and prints
every number from 0 to max (not inclusive) that is divisible by
either 3 or 5, but not both.
*/

fizzBuzz= (nums) => {
    console.log(nums)

    for (let i in nums ){
        console.log(i)
    }

}



fizzBuzz(20)
