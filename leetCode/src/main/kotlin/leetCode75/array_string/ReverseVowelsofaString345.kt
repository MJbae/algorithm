package leetCode75.array_string

fun main() {
    val result = Solution5a().reverseVowels("hello")

    println(result)
}

class Solution5a {
    fun reverseVowels(s: String): String {
        val result = StringBuilder(s)

        val vowelsMap = extractVowels(s)

        reverseVowels(result, vowelsMap)

        return result.toString()
    }

    private fun extractVowels(s: String): MutableMap<Int, Char>{
        val vowels = listOf('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        val vowelsMap: MutableMap<Int, Char> = mutableMapOf()
        val result = StringBuilder(s)

        for (index in result.indices){
            if(result[index] in vowels){
                vowelsMap[index] = result[index]
            }
        }

        return vowelsMap
    }
    private fun reverseVowels(result: StringBuilder, vowelsMap: MutableMap<Int, Char>) {
        val keys = vowelsMap.keys.toList()
        val valuesReverse = vowelsMap.values.reversed()

        for ((key, value) in keys.zip(valuesReverse)){
            result[key] = value
        }
    }
}
