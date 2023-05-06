package leetCode75.array_string

fun main() {
    val result = Solution2_1().gcdOfStrings("leet", "code")
    println(result)
}

// Time Limit Exceeded
class Solution2_1 {
    fun gcdOfStrings(str1: String, str2: String): String {

        // get min length btw strings
        // set base with the min
        var base = if (str1.length < str2.length) str1 else str2

        // check the base is gcd
        // 1. the length of the base should be dividable
        // 2. length(str/base) times the substring should work
        while (base.isNotEmpty()) {
            // if it is, return the base
            if (valid(base, str1, str2)) return base

            // if it is not, remove one char from the right of the base
            base = base.removeSuffix(base.last().toString())
        }
        return ""
    }

    private fun valid(gcd: String, str1: String, str2: String): Boolean {
        var str1Copy = str1
        var str2Copy = str2

        while (str1Copy.length != gcd.length || str2Copy.length != gcd.length) {
            if (str1Copy.length % gcd.length != 0) return false
            if (str2Copy.length % gcd.length != 0) return false

            if (str1Copy.length > gcd.length) {
                str1Copy = str1Copy.removePrefix(gcd)
            }
            if (str2Copy.length > gcd.length) {
                str2Copy = str2Copy.removePrefix(gcd)
            }
        }

        if (!str1Copy.startsWith(gcd)) return false
        if (!str2Copy.startsWith(gcd)) return false

        return true
    }
}