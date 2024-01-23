
//! 1- a question from Ai training
/*

What Javascript statement in place of "?" will make the result always be between 6 and 7?
 const x = 2;
 let y = 4;
 function update(arg)
 { return Math.random() + y * arg; }
 y = 2;
  ?;
  const result = update(x); *
*/

const x = 2;
let y = 4;

function update(arg) {
    return Math.random() + y * arg;
}

y = 2;
//   ?;
y = (8 - x) / x;
// or (because he said x is const )
// y = 3

const result = update(x);

console.log(result)
