let num = [0, 1, 0, 3, 12]

function check(numbers) {

    for (let i in numbers) {

        number = numbers[i]
        if (number == 0) {

            let num1 = numbers.splice(i, 1)
            console.log(num1)
            numbers.push(number)
        }

    }

    console.log(numbers)

}

check(num)
