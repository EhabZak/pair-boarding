

 function num(n){
    let result = ''
    for (let int of n){
        console.log(int)

        if (int === '0'){

            int = "1"
            result+=int
        }else{
            int ="0"
            result+=int
        }
    }
    return result

}

console.log(num('10000'))
