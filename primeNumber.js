const primeNumber = (numbers) => {
  let primeNumbers = [];
  for (let i = 0; i < numbers.length; i++) {
    let isPrime = true;
    for (let j = 2; j < numbers[i]; j++) {
      if (numbers[i] % j === 0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime) {
      primeNumbers.push(numbers[i]);
    }
  }
  return primeNumbers;
};

// Test the function
const numbers = [11, 2, 3, 4, 5, 6, 7]
console.log(primeNumber(numbers));
numbers.sort((a, b) => a - b);
numbers.push(8);
console.log(numbers) 