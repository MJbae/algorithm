package leetCode75.array_string

fun main() {
    val result = Solution3Best().kidsWithCandies(intArrayOf(12, 1, 12), 10)
    println(result)
}

class Solution3a {
    fun kidsWithCandies(candies: IntArray, extraCandies: Int): List<Boolean> {
        val maxCandy = candies.max()
        return candies.map { candy -> checker(candy as Int, maxCandy as Int, extraCandies as Int) }.toList()
    }

    private fun checker(candy: Int, maxCandy: Int, extraCandies: Int): Boolean {
        if (candy == maxCandy) return true

        val candidate = candy + extraCandies
        if (candidate >= maxCandy) return true
        return false
    }
}

class Solution3Best {
    fun kidsWithCandies(candies: IntArray, extraCandies: Int): List<Boolean> {
        val max = candies.max() ?: 0
        return candies.mapIndexed { _, value ->
            value + extraCandies >= max
        }
    }
}
