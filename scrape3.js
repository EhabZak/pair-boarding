// //! Time conversion
// function timeConversion(s) {
//     // Write your code here

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


let input = "07:05:45PM"  // output 19:05:45
// let input = "12:05:45AM"

// let input = "07:05:45AM"
// 19:05:45


//!
function timeConversion(s) {

    let time = input.slice(-2)

    let [hour, min, sec]= s.slice(0,-2).split(':')
    console.log(hour)

    if (time ==='PM'){

        if (hour != '12'){
            hour = String(Number(hour)+ 12)
        }else{
            if (hour === '12'){
                hour = '00'
            }
        }

  
