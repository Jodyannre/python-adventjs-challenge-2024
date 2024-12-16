
function main() {

    let dataSet2 = [
        { "name": 'Alice', "city": 'London' },
        { "name": 'Bob', "city": 'Paris' },
        { "name": 'Charlie', "city": 'New York' }
        ]
    
        let dataSet = [
            {"gift": 'Doll', "quantity": 10},
            {"gift": 'Book', "quantity": 5},
            {"gift": 'Music CD', "quantity": 1}
        ]
    
        dataSet2 = [
            { "name": 'Alice', "city": 'London' }
        ]
    
        dataSet2 = [
          { "game": 'indianajones', "subtitle": 'the game'},
        { "game": 'pokemonblue', "subtitle": ''}
        ]
    
        console.log(drawTable(dataSet))

}
    
 /* Por alguna extraña razón no pasa los test en la página, pero las respuestas son las mismas que las esperadas*/
function drawTable(data) {
    let keys = Object.keys(data[0])
    let max_width = []
    let result = ""
    let top_bottom_border = ""
    let header = ""

    //Capitalizar la primera letra de cada key
    const capitalize = (str) => str.charAt(0).toUpperCase() + str.slice(1);

    //Obtener maximo ancho de cada columna
    max_width = keys.map(key => Math.max(
        key.length,
        ...data.map(row => row[key].toString().length)
    ))

    //Construir borders superior, inferior y primera fila de la tabla con keys capitalizadas
    keys.map((key, i) => {
        top_bottom_border +=`+${'-'.repeat((max_width[i] + 2))}`
        header += `| ${capitalize(key)}${" ".repeat((max_width[i] - key.length))} `
    })

    //Construir cuerpo de la tabla
    data.map(row => {
        result += `|${keys.map((key,i)=> {
            const cell = row[key].toString()
            return ` ${cell}${" ".repeat(max_width[i] - cell.length)} `
        }).join("|")}|\n`
    })
    
    //Agregar border inferior de la tabla
    result = top_bottom_border + "+\n" + header + "|\n" + top_bottom_border + "+\n" + result + top_bottom_border + "+"

    return result
}
    
main()




/*
function drawTable(data) {
    let dataSet = data
    let keys = Object.keys(dataSet[0])
    let max_width = []
    let values = []
    let result = ""
    let acc_data = null
    let top_bottom_border = ""
    let acc = null

    //Capitalizar la primera letra de cada key
    const capitalize = (str) => str.charAt(0).toUpperCase() + str.slice(1);
    

    //Inicializar arrays max_width y values
    keys.forEach((d) => {
        max_width.push(d.length)
        values.push([])
    })

    //Obtener maximo ancho de cada columna
    dataSet.forEach((data) => {
        keys.forEach((name,key) => {
            acc_data = data[name]
            max_width[key] = Math.max(max_width[key], acc_data.toString().length)
            values[key].push(acc_data)
        })
    })

    let key = 0

    //Construir borders superior, inferior y primera fila de la tabla con keys capitalizadas
    for (key; key < keys.length; key++) {
        top_bottom_border +=`+${'-'.repeat((max_width[key] + 2))}`
        result += "|" + " " + capitalize(keys[key]) + " ".repeat((max_width[key] - keys[key].length)) + " "
    }
    result = top_bottom_border + "+\n" + result + "|\n" + top_bottom_border + "+\n"

    //Construir cuerpo de la tabla
    for (let j=0; j < dataSet.length; j++) {
        for (let i=0; i < keys.length; i++) {
            acc = values[i][j].toString()
            result += "|" + " " + acc + " ".repeat((max_width[i] - acc.length)) + " "
        }
        result += "|\n"
    }

    //Agregar border inferior de la tabla
    result += top_bottom_border + "+"

    return result
}

*/