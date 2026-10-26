class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        const map = new Map();

        for (let i = 0; i < nums.length; i++) {
            let val = map.get(nums[i])
            if (val) {
                map.set(nums[i], val + 1)
            } else {
                map.set(nums[i], 1)
            }
        }

        const arr = []
        for (let [num, count] of map.entries()){       arr.push([num, count])
        }

        arr.sort((a, b) => b[1] - a[1])

        const res = []

        console.log(arr)

        while (res.length < k) {
            res.push(arr.shift()[0])
        }

        return res
    }
}
