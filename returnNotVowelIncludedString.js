arr = ["My", "Hai", "Dry", "sync", "Are", "You"];


const vowelString = "aeiou"



const arrWithNoVowelWords = []

for(const word of arr){
    let flag = 0
    for (const c of word){
        if (vowelString.includes( c.toLowerCase())){
            flag = 1
            break
        }
    }
    if (flag == 0) {
        arrWithNoVowelWords.push(word)
    } 
}

console.log(arrWithNoVowelWords)

// single line with regular expression and filter method
const result = arr.filter(word=>  !/[aeiou]/i.test(word))

console.log('result is :',result)