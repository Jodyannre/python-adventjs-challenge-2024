function findInAgenda(agenda, phone) {
    let count = 0;
    let result = {};

    const configResult = (line) => {

        let i1 = undefined
        let i2 = undefined

        const match = line.match(/<(?<name>[^>]+)>/);
        if (match) {
            result = {
                name: match.groups.name,
                address: line.replace(match[0], '').trim(),
            };


        for (let i = 0; i < line.length; i++) {
            const char = line[i];
    
            if (char == '+' && i1 === undefined) {
                i1 = i;
                i2 = i1 + 14;
            }
            if (i1 !== undefined) {
                break;
            }
        }
        
        if (i3 == 0 && i2 >= line.length-2) /* El address esta en medio */ {
            result.addres = line.substring(i4+1, i1-1).trim();
        } else
        if (i4 >= line.length-2 && i1 == 0) /* El address esta en medio */ {
            result.address = line.substring(i2+1, i3-1).trim();
        } else
        if (i4 >= line.length-2) {
            result.address = line.substring(0, i1-1).trim();
        } else {
            result.address = line.substring(0, i3-1).trim();
        }

        result.name = line.substring(i3+1, i4);
    }
}

    for (let line of agenda.split('\n')) {
        if (line.includes(phone)) {
            count++;
            if (count > 1) {return null;}
            configResult(line);
        }
    }
    
    return count === 0 ? null : result;
  
}
const agenda = `+34-600-123-456 Calle Gran Via 12 <Juan Perez>\n
Plaza Mayor 45 Madrid 28013 <Maria Gomez> +34-600-987-654\n
<Carlos Ruiz> +1-800-555-0199 Fifth Ave New York`

console.log(findInAgenda(agenda, '34-600-123-456'))
// { name: "Juan Perez", address: "Calle Gran Via 12" }


console.log(findInAgenda(agenda, '600-987'))
// { name: "Maria Gomez", address: "Plaza Mayor 45 Madrid 28013" }


console.log(findInAgenda(agenda, '111'))
// null
// Explanation: No results

console.log(findInAgenda(agenda, '1'))