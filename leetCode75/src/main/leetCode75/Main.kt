fun main() {
    println(Solution().solution(0))
}


class Solution {
    fun solution(num: Int): String {
        return if (num % 2 == 0) "Even" else "Odd"
    }
}