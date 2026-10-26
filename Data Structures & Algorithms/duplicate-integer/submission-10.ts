class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const dict: Record<number, number> = {}

        nums.forEach(n => {
            if (dict[n]) {
               dict[n] += 1 
            } else {
                dict[n] = 1
            }
        })

        console.log(dict)

        return Object.entries(dict).some(([key, value]) => value > 1)
    }
}
