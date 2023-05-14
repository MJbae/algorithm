package leetCode75.array_string

fun main() {
    val result = Solution5a().reverseVowels("hello")

    println(result)
}

class Solution5a {
    fun reverseVowels(s: String): String {
        val vowels = listOf('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        val stringMap: MutableMap<Int, Char> = mutableMapOf()
        val result = StringBuilder(s)

        for (index in result.indices){
            if(result[index] in vowels){
                stringMap[index] = result[index]
            }
        }

        val keys = stringMap.keys.toList()
        val valuesReverse = stringMap.values.reversed()

        for (index in keys.indices){
            val key = keys[index]
            val value = valuesReverse[index]
            result[key] = value
        }

        return result.toString()
    }
}
