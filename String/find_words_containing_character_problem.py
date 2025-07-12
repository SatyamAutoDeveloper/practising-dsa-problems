class FindWordsContainingChar():
    def findWordsContaining(self, words, x):
        indices = []
        for idx in range(len(words)):
            if x in words[idx]:
                indices.append(idx)
        return indices

fwcc = FindWordsContainingChar()
print("Array of Indices contains X in words ::", fwcc.findWordsContaining(["qyfxur"], "r"))


"""
The time complexity of the findWordsContaining method is O(n * m), where n is the number of words in the list (len(words)) and m is the maximum length of a word in the list. This is because for each word, the method checks whether the character x is present, which in the worst case requires scanning through the entire word.

The space complexity is O(k), where k is the number of indices stored in the indices list. In the worst case, if every word contains the character x, the list will store n indices, so space complexity is O(n). Other variables used (like the indices list and loop counters) require constant space, so overall space complexity is dominated by the size of the output list.
"""