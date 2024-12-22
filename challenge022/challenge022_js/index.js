function main() {
    console.log(generateGiftSets(['car', 'doll']));
    //console.log(generateGiftSets(['1', '2', '3']));
}

function generateGiftSets(gifts) {
    const result = [];
    const level = gifts.length + 1;

    // Función para agregar elementos al array de resultados
    function addToArray(arr) {
        for (const elm of arr) {
            if (!Array.isArray(elm)) {
                result.push([elm]);
            } else {
                result.push(elm);
            }
        }
    }

    // Función recursiva para generar combinaciones
    function recorrer(arr, level, acc) {
        if (level === 1) {
            return arr.slice(acc);
        } else {
            return arr.slice(acc).flatMap((y, idx) => 
                recorrer(arr, level - 1, arr.indexOf(y) + 1).map(x =>
                    Array.isArray(x) ? [y, ...x] : [y, x]
                )
            );
        }
    }

    // Ejecutar el algoritmo
    for (let i = 1; i < level; i++) {
        const temp = recorrer(gifts, i, 0);
        addToArray(temp);
    }

    return result;
}

// Llamada a la función principal
main();