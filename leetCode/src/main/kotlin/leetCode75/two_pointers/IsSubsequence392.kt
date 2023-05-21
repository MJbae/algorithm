package leetCode75.two_pointers

fun main() {
    val result = Solution2a().isSubsequence("aaaaaa", "bbaaaa")
    println("result: $result")
}

// fail
class Solution2a {
    fun isSubsequence(s: String, t: String): Boolean {
        // t의 요소를 앞에서부터 제거하면서 인덱스 저장
        var lastCharAt = 0
        var matchCount = 0
        s.forEach outer@{ sChar ->
            t.forEachIndexed inner@{ index, c ->
                if (sChar == c) {
                    // 만약 s의 다음 요소의 인덱스가 전 인덱스가 작으면 false 반환
                    if (index < lastCharAt) return false

                    lastCharAt = index
                    matchCount++
                    return@outer
                }
            }
        }

        // s 내 문자가 t에서 모두 발견되지 않으면 false 반환
        return matchCount == s.length
    }
}

// space complexity: O(1), time complexity: O(n)
class Solution2Best {
    fun isSubsequence(s: String, t: String): Boolean {
        var sIndex = 0
        var tIndex = 0
        while (sIndex < s.length && tIndex < t.length) {
            if (s[sIndex] == t[tIndex]) {
                sIndex++
            }
            tIndex++
        }
        return sIndex == s.length
    }
}
