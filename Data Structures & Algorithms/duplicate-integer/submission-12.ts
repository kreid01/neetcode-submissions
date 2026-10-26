class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        let map: Map<number, number> = new Map();
        let found = false;

        nums.map(x => {
            let val = map.get(x)
            if (val) {
                found = true
            } else {
                map.set(x, 1)
            }
        })

        return found
    }
}
