class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        let map: Map<number, number> = new Map();
        nums.map(x => {
            let val = map.get(x)
            if (val) {
                map.set(x, val + 1)
            } else {
                map.set(x, 1)
            }
        })

        for (const v of map.values()) {
            if (v as any > 1) {
                return true
            }
        }

        return false
    }
}
