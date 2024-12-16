/**
 * @param {string} s
 * @returns {string}
 */
function removeSnow(s: string): string {
    if (s.length === 0) return s
    
    return s.split('').reduce((acc, curr) => {
        if (curr === acc[acc.length - 1]) {
            return acc.substring(0, acc.length - 1)
        }
        return acc + curr 
        })
  }


  removeSnow("zxxzoz")
  removeSnow("abcdd")
  removeSnow("zzz")
  removeSnow("a")