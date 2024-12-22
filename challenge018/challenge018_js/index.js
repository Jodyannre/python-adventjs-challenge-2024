function findInAgenda(agenda, phone) {
    const regex = new RegExp(`^.*${phone}.*(?:\n|$)`, 'gm'); 
    const name = /<([^>]+)>/;
    let matches = [...agenda.matchAll(regex)];
    let result = {}
    if (matches.length < 2) {
        let newLine = matches[0][0].replace("+"+phone, '');
        let names = newLine.match(name);
        let addres = newLine.replace(names[0], '').trim();
        result = {
            name: names[1],
            address: addres
        }
        //console.log(names[1]);
        //console.log(addres);
    }

    return result;
}





const agenda = `+34-600-123-456 Calle Gran Via 12 <Juan Perez>\n
Plaza Mayor 45 Madrid 28013 <Maria Gomez> +34-600-987-654\n
<Carlos Ruiz> +1-800-555-0199 Fifth Ave New York`

console.log(findInAgenda(agenda, '34-600-123-456'))
// { name: "Juan Perez", address: "Calle Gran Via 12" }



console.log(findInAgenda(agenda, '600-987'))
// { name: "Maria Gomez", address: "Plaza Mayor 45 Madrid 28013" }

/*
console.log(findInAgenda(agenda, '111'))
// null
// Explanation: No results

console.log(findInAgenda(agenda, '1'))

*/