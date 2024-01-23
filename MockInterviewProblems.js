
//! where is the first mock interview question  ?????????????????




//! 2-Second Mock Interview

var romanToInt = function(s) {
    let total = 0
    const convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for (let i = 0; i < s.length; i++) {
        total += convert[s[i]]
    }

    for (let i = 0; i < s.length-1; i++) {
        if (convert[s[i]] < convert[s[i+1]]) {
            total -= 2 * convert[s[i]]
        }
    }
    return total
};
