const numOfOcc = (word) => {
  const a = word.split(""); 
  const letters = {};

  for (let i = 0; i < a.length; i++) {

    if (a[i] in letters) {
      letters[a[i]] += 1; 
    } else {
      letters[a[i]] = 1;
    }
  }

  return letters; 
};

const word = "HAPPY";
const val = numOfOcc(word);
console.log(val);
