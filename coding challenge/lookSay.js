// INVERSE LOOK AND SAY

const lookSay = number => {
    let num = String(number)

    let result = ""
    let i = 0

    while (i < num.length) {
        let count = 1
        while ((i + 1 < num.length) && num[i] === num[i+1]){
            i += 1
            count += 1
        }
        result += (String(count) + num[i])
        i += 1
    }

    return result
}

number = 124324

console.log(lookSay(number));