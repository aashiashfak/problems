word = "Hello ";

lower = 0
upper = 0

word.split('').forEach(element => {
    if (element === element.toUpperCase() && element !== element.toLowerCase()){
        upper ++ 
    }else if (element === element.toLowerCase() && element !== element.toUpperCase()){
        lower ++
    }
});

console.log('upper:',upper);
console.log('lower:',lower);



