class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        if (strs.length == 1) {
            return [strs]
        }

        let grams = new Map()

        let sorted = strs.map(x => x.split("").sort().join(""))
        for (let i = 0; i < strs.length; i++) {
            if (grams.get(sorted[i])) {
                grams.set(sorted[i], [...grams.get(sorted[i]), strs[i]])
            } else {
                grams.set(sorted[i], [strs[i]])
            }
        }        


        let res = []
        for (const g of grams.values()) {
            res.push(g)
        }

        return res
    }
}
