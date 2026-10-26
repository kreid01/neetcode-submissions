class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        let map: Map<number, number> = new Map();

        for (const num of nums) {
            if (map.get(num)) {
                return true
            } else {
                map.set(num, 1)
            }
        }

        return false
    }
}
