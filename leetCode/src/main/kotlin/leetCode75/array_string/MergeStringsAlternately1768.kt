package leetCode75.array_string

fun main() {
    val result = Solution1Best().mergeAlternately("abc", "pqr")
    println(result)
}

// Time Complexity is O(max(n,m))
class Solution1a {
    fun mergeAlternately(word1: String, word2: String): String {
        var result = ""
        for (i in 0..Math.max(word1.length - 1, word2.length - 1)) {
            if (i < word1.length) result += word1[i]
            if (i < word2.length) result += word2[i]
        }

        return result
    }
}

class Solution1b {
    fun mergeAlternately(word1: String, word2: String): String {
        var result = ""
        var i = 0
        while (i < word1.length || i < word2.length) {
            if (i < word1.length) result += word1[i]
            if (i < word2.length) result += word2[i]

            i++
        }

        return result
    }
}

class Solution1Best {
    fun mergeAlternately(word1: String, word2: String): String {
        val result = StringBuilder()
        var i = 0

        while (i < word1.length || i < word2.length) {
            if (i < word1.length) result.append(word1[i])
            if (i < word2.length) result.append(word2[i])

            i++
        }

        return result.toString()
    }
}

class Solution1d {
    fun mergeAlternately(word1: String, word2: String): String {
        val result = StringBuilder()
        val maxIdx = Math.max(word1.length - 1, word2.length - 1)

        for (i in 0..maxIdx) {
            if (i < word1.length) result.append(word1[i])
            if (i < word2.length) result.append(word2[i])
        }

        return result.toString()
    }
}
