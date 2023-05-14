package leetCode75.array_string

fun main() {
    val result = Solution5a().reverseVowels("hello")

    println(result)
}

class Solution5a {
    fun reverseVowels(s: String): String {
        val vowels = listOf('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        val charMap: MutableMap<Int, Char> = mutableMapOf()
        val result = StringBuilder(s)

        for (index in result.indices){
            if(result[index] in vowels){
                charMap[index] = result[index]
            }
        }

        val keys = charMap.keys.toList()
        val valuesReverse = charMap.values.reversed()
        val reversedChar = keys.zip(valuesReverse)

        for ((key, value) in reversedChar){
            result[key] = value
        }

        return result.toString()
    }
}
