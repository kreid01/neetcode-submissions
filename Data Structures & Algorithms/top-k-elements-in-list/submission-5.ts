class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        let freq: Record<number, number> = {}

        for (let i = 0; i < nums.length; i++) {
            if (freq[nums[i]]) {
                freq[nums[i]] += 1
            } else {
                freq[nums[i]] = 1
            }
        }
        
        return Object.entries(freq).sort((a, b) => b[1] - a[1]).slice(0, k).map(([k, v]) => parseInt(k))

    }
}
