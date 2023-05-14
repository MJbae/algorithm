package leetCode75.array_string

fun main() {
    val result = Solution4a().canPlaceFlowers(flowerbed = intArrayOf(1, 0, 0, 0, 1), n = 1)
    println(result)
}

// Fail to satisfy testcases
class Solution4a {
    fun canPlaceFlowers(flowerbed: IntArray, n: Int): Boolean {
        if (flowerbed.isEmpty()) return false
        if (flowerbed.size == 1 && flowerbed[0] == 0) return true

        val possibleFollowers = getPlantableFlowers(flowerbed)

        return possibleFollowers >= n
    }

    private fun getPlantableFlowers(flowerbed: IntArray): Int {
        var result = 0
        val size = flowerbed.size

        if (flowerbed.size >= 3 && flowerbed[0] == 0 && flowerbed[1] == 0 && flowerbed[2] == 1) {
            flowerbed[0] = 1
            result++
        }

        // array 순회 중 0인 요소 선택
        for (index in 1 until (size - 1)) {
            if (flowerbed[index] == 0) {
                // 0인 요소의 앞뒤 요소가 1이면 집계 x
                if (flowerbed[index - 1] == 1 || flowerbed[index + 1] == 1) {
                    continue
                }
                flowerbed[index] = 1
                result++
            }

        }

        if (flowerbed.size >= 3 && flowerbed[size-3] == 1 && flowerbed[size-2] == 0 && flowerbed[size-1] == 0) result++

        return result
    }
}
