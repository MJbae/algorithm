package leetCode75.sliding_windows

fun main() {
    val nums = intArrayOf(1, 12, -5, -6, 50, 3)
    val result = Solution1a().findMaxAverage(nums, k = 4)
    println("result: $result")
}

// Fail Time Limit Exceeded
class Solution1a {
    fun findMaxAverage(nums: IntArray, k: Int): Double? {
        var result: Double? = null
        var temp: Double?
        var firstIdx = 0

        if (nums.size == k) return calMaxArray(nums, firstIdx, k)

        while (nums.size - k >= firstIdx) {
            temp = calMaxArray(nums, firstIdx, k)

            if (result == null) {
                result = temp
            }
            if (temp > result) result = temp

            firstIdx++
        }

        return result
    }

    private fun calMaxArray(nums: IntArray, firstIdx: Int, size: Int): Double {
        var sum = 0.0
        (0 until size).forEach {
            sum += nums[firstIdx + it]
        }

        return sum / size
    }
}


// Sliding Window 활용
class Solution1Best {
    class Solution {
        fun findMaxAverage(nums: IntArray, k: Int): Double {
            val kDouble = k.toDouble()
            var currAvg = 0.0
            for (i in 0 until k) {
                currAvg += nums[i] / kDouble
            }

            var answer = currAvg
            for (i in k .. nums.lastIndex) {
                currAvg -= nums[i - k] / kDouble
                currAvg += nums[i] / kDouble
                answer = maxOf(answer, currAvg)
            }

            return answer
        }
    }
}