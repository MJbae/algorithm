package leetCode75.two_pointers

fun main() {
    val nums = intArrayOf(0, 1, 0, 3, 12)
    Solution1a().moveZeroes(nums)
    nums.forEach { println(it) }
}

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