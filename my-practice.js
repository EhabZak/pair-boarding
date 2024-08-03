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


// reverse = (Name) =>{
//     let Name2 =''

//     for (let i = Name.length-1; i >= 0; i--) {

//         Name2 += Name[i]

//     }
//     return Name2
// }

// console.log(reverse('zak'))



/*
Define a function fizzBuzz(max) that takes a number and prints
every number from 0 to max (not inclusive) that is divisible by
either 3 or 5, but not both.
*/




// let array = [["a", "b", "c"], ["d", "e"], ["f", "g", "h"]];

/*
input = 1
1-convert to 32 ok
Binary representation: 00000000000000000000000000000001 ok
2-Flipping the bits: 11111111111111111111111111111110 ok
3-Decimal value of the flipped bits: 4294967294
*/



function flippingBits(n) {
    // Convert number to a 32-bit integer using bitwise OR
    let int32 = n | 0

    // Convert to binary string

    let binaryStr = int32.toString(2)

    // Pad with leading zeros to ensure 32 bits
    let binaryZero = binaryStr.padStart(32,'0')

    let res = ''

    for (let int of binaryZero){
        // console.log(int)

        if (int === '0'){
            int = "1"
            res +=int
        }else{
            int ="0"
            res +=int

        }
    }

  
