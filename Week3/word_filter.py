"""
Word Filter and Counter Function

Objective:
Write a function named 'word_filter_counter' that filters and counts specific words in a given text.

Function Parameters:
1. text (string): The text from which words will be filtered and counted.
2. filter_words (list of strings): A list of words to be filtered out from the text.

Instructions:
- The function should filter out the words from the text that are present in the filter_words list. The comparison should be case-insensitive.
- The function should return a dictionary. In this dictionary, the keys are the filtered words, and the values are the counts of how often these words appeared in the text.
- The text may contain punctuation marks and spaces. Only whole words, separated by spaces or punctuation, should be considered.

Example Test Cases:
1. word_filter_counter("Hello world, hello!", ["hello"]) should return a dictionary with the count of occurrences of "hello".
2. word_filter_counter("The quick brown fox.", ["the"]) should return a dictionary with the count of occurrences of "the".
3. word_filter_counter("Is this real life? Is this just fantasy?", ["is", "this", "just"]) should return a dictionary with the counts of occurrences of "is", "this", and "just".
4. word_filter_counter("Do we see the big picture or just small details?", ["we", "the", "or"]) should return a dictionary with the counts of occurrences of "we", "the", and "or".
"""

#思路：分割语句的每个单词，然后查看filter的单词在不在text里，每在1次计数+1，不在则为0
import string
def word_filter_counter(text, filter_words):
    word_filter = {}
    scope = len(filter_words)
    #通过将长度赋给变量 scope，可以避免重复计算。
    text_lower = text.lower()
    text_list =text_lower.translate(str.maketrans("","",string.punctuation))
    """
    string.punctuation 是字符串模块中提供的一个包含所有标点符号的字符串。
    str.maketrans("", "", string.punctuation) 创建了一个转换表，该表将标点符号映射为空字符 ("")，即删除标点符号。
    text_lower.translate(...) 使用上述转换表将 text_lower 中的字符进行相应的映射。由于标点符号被映射为 None 因此它们会被删除。
    最终text_list 包含了去除了标点符号的小写文本。
    """
    for i in range(scope):
     word_filter[filter_words[i]] = text_list.count(filter_words[i])
    return word_filter
"""
for i in range(scope):: 这是一个 for 循环，用于遍历 filter_words 列表中的每个单词。scope 是在之前定义的变量，可能是 filter_words 列表的长度。

word_filter[filter_words[i]] = text_list.count(filter_words[i]): 在每次循环中，统计 text_list 中当前单词 filter_words[i] 的出现次数，然后将结果存储在字典 word_filter 中，以该单词为键，出现次数为值。

注意，此处使用了 text_list.count(filter_words[i]) 来获取在 text_list 中单词出现的次数。
count()是string的内置方法 用于统计某个元素在字符串或列表中出现的次数 所以一开始要 import string

在字典中，使用方括号 [] 来访问键对应的值。如果字典中存在该键，就会返回对应的值；如果不存在，会引发 KeyError。

循环结束后，返回字典 word_filter。

请注意，可能存在一些改进的空间，例如使用字典的 get 方法来处理不存在的键，以避免 KeyError。这样可以更稳健地处理统计过程。"""

    # Your code goes here
    # Implement the logic to filter words and count their occurrences
    


# Test cases
print(
    word_filter_counter("Hello world, hello!", ["hello"])
)  # Expected output: {'hello': 2}
print(
    word_filter_counter("The quick brown fox.", ["the"])
)  # Expected output: {'the': 1}
print(
    word_filter_counter(
        "Is this real life? Is this just fantasy?", ["is", "this", "just"]
    )
)  # Expected output: {'is': 2, 'this': 2, 'just': 1}
print(
    word_filter_counter(
        "Do we see the big picture or just small details?", ["we", "the", "or"]
    )
)  # Expected output: {'we': 1, 'the': 1, 'or': 1}
