word = 'ammad'

const CheckPalindrom = ((word)=>{
    l = word.length
    for (let i=0 ; i<=l/2 ; i++){
        if (word[i] !== word[l-i-1]) return 'this is not palindrome'
    }
    return 'this is palindrome'
})

console.log(CheckPalindrom(word));
console.log(Math.floor(5/3));



w