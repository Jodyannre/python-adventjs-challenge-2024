console.log("Hello via Bun y lo demas!");


function calculatePrice(ornaments: string): number | undefined {
    const prices = new Map<string, number>([
       [ '*', 1],['o', 5],['^', 10],['#', 50],['@', 100]
    ]);
    let  actual: number | undefined = -1
    let  prev = -1
    let  result = 0
  
      for (let ornament of ornaments.split('').reverse()) {
          actual = prices.get(ornament) || undefined
            if (actual === undefined) {
                return undefined
            }
          result += prev <= actual? actual: -actual
          prev = actual
      }
    return result     
  }

calculatePrice('***')  // 3   (1 + 1 + 1)
calculatePrice('*o')   // 4   (5 - 1)
calculatePrice('o*')   // 6   (5 + 1)
calculatePrice('*o*')  // 5  (-1 + 5 + 1) 
calculatePrice('**o*') // 6  (1 - 1 + 5 + 1) 
calculatePrice('o***') // 8   (5 + 3)
calculatePrice('*o@')  // 94  (-5 - 1 + 100)
calculatePrice('*#')   // 49  (-1 + 50)
calculatePrice('@@@')  // 300 (100 + 100 + 100)
calculatePrice('#@')   // 50  (-50 + 100)
calculatePrice('#@Z')  // undefined (Z is unknown)




  