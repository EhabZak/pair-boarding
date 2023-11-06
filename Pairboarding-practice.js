//! digitalRoot

/*
Write a method, digitalRoot(num). It should sum the digits of a positive integer.
 If it is greater than or equal to 10, sum the digits of the resulting number.
 Keep repeating until there is only one digit in the result, called the "digital root".
  Do not use string conversion within your method.
*/

function digitalRoot(num) {
    while (num > 10) {
      num = digitalRootStep(num);
    }

    return num;
  }

  function digitalRootStep(num) {
    let root = 0;

    while (num > 0) {
      root += num % 10;
      num = Math.floor(num/10);
    }

    return root;
  }

  // Alternate solution
  function digitalRoot(num) {
    const digits = [];

    while (num > 0) {
      digits.push(num % 10);
      num = Math.floor(num/10);
    }

    const digitSum = digits.reduce((sum, digit) => sum + digit);
    return digitSum > 10 ? digitalRoot(digitSum) : digitSum;
  }

  // Magical one-line solution
  function digitalRoot(num) {
    return num < 10 ? num : digitalRoot(digitalRoot(Math.floor(num / 10)) + (num % 10));
  }
 //! caesarCipher

 /*Write a function that takes a message and an increment amount and outputs the
  same letters shifted by that amount in the alphabet. Assume lowercase and no punctuation.
   Preserve spaces. */

   function caesarCipher(str, shift) {
    const alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');
    let encoded = "";

    for (let i = 0; i < str.length; i++) {
      if (str[i] === ' ') {
        encoded += ' ';
        continue;
      }

      const offset = (alphabet.indexOf(str[i]) + shift) % 26;
      encoded += alphabet[offset];
    }

    return encoded;
  }

  // fibsSum

  /*
Write a function, fibsSum(n), that finds the sum of the first n fibonacci numbers
 recursively. Assume n > 0. Note that for this problem, the fibonacci sequence starts
 with [1, 1].
  */
