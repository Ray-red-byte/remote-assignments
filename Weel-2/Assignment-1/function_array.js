function max(numbers) {
    if (numbers.length === 0){
        return 'Empty List'
    }

    var max = numbers[0]
    for (number of numbers){
        if (number > max){
            max = number
        }
    }
    return max
}


function findPosition(numbers, target) {
    for (let i = 0; i < numbers.length; i++){
        if (numbers[i] === target){
            return i
        }
    }

    return -1
}



console.log( max([1, 2, 4, 5]) );
console.log( max([5, 2, 7, 1, 6]) );
console.log( findPosition([5, 2, 7, 1, 6], 5) );
console.log( findPosition([5, 2, 7, 1, 6], 7) );
console.log( findPosition([5, 2, 7, 7, 7, 1, 6], 7) );
console.log( findPosition([5, 2, 7, 1, 6], 8) );