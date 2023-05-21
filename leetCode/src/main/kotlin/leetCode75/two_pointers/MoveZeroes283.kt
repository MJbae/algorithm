package leetCode75.two_pointers

fun main() {
    val nums = intArrayOf(0, 1, 0, 3, 12)
    Solution1Best().moveZeroes(nums)
    nums.forEach { println(it) }
}

// space complexity: O(n), time complexity: O(n)
class Solution1a {
    fun moveZeroes(nums: IntArray) {
        val answer = mutableListOf<Int>()

        nums.forEach {
            if (it != 0) answer.add(it)
        }

        val zeroCounts = nums.size - answer.size

        (0 until zeroCounts).forEach {
            answer.add(0)
        }

        answer.forEachIndexed { index, value ->
            nums[index] = value
        }
    }
}

// space complexity: O(1), time complexity: O(n)
class Solution1b {
    fun moveZeroes(nums: IntArray) {
        var lastNoneZeroAt = 0

        nums.forEach {
            if (it != 0) {
                nums[lastNoneZeroAt] = it
                lastNoneZeroAt++
            }
        }

        (lastNoneZeroAt until nums.size).forEach {
            nums[it] = 0
        }
    }
}

// space complexity: O(1), time complexity: O(n)
// better when most elements are 0
class Solution1Best {
    fun moveZeroes(nums: IntArray) {
        var lastNoneZeroAt = 0

        nums.forEachIndexed { index, value ->
            if (value != 0) {
                swap(nums, lastNoneZeroAt, index)
                lastNoneZeroAt++
            }
        }
    }

    private fun swap(nums: IntArray, lastNoneZeroAt: Int, index: Int) {
        nums[lastNoneZeroAt] = nums[index].also { nums[index] = nums[lastNoneZeroAt] }
    }
}