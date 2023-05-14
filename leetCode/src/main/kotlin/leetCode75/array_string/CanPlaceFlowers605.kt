package leetCode75.array_string

fun main() {
    val result = Solution4a().canPlaceFlowers(flowerbed = intArrayOf(1, 0, 0, 0, 1), n = 1)
    println(result)
}

class Solution4a {
    fun canPlaceFlowers(flowerbed: IntArray, n: Int): Boolean {
        if (flowerbed.isEmpty()) return false

        val possibleFollowers = getPlantableFlowers(flowerbed)

        return possibleFollowers >= n
    }

    private fun getPlantableFlowers(flowerbed: IntArray): Int {
        var result = 0

        for (index in flowerbed.indices) {
            if (flowerbed[index] == 0
                && isLeftEmpty(flowerbed, index)
                && isRightEmpty(flowerbed, index)
            ) {
                flowerbed[index] = 1
                result++
            }

        }

        return result
    }

    private fun isLeftEmpty(flowerbed: IntArray, index: Int): Boolean {
        return index == 0 || flowerbed[index - 1] == 0
    }

    private fun isRightEmpty(flowerbed: IntArray, index: Int): Boolean {
        return index == (flowerbed.size - 1) || flowerbed[index + 1] == 0
    }
}

class Solution4b {

    fun canPlaceFlowers(flowerbed: IntArray, n: Int): Boolean {

        var cnt = 0

        for (i in flowerbed.indices) {

            val prev = flowerbed.getOrNull(i - 1)
            val validPrev = prev == null || prev == 0
            val next = flowerbed.getOrNull(i + 1)
            val validNext = next == null || next == 0

            if (validPrev && validNext && flowerbed[i] == 0) {
                flowerbed[i] = 1
                cnt++
            }
        }

        return cnt >= n
    }
}
