class MostWordsFound():
    def mostWordsFound(self, sentences):
        mostwords = 0
        for sentence in sentences:
            wordcount = sentence.count(" ") + 1
            if wordcount > mostwords:
                mostwords = wordcount 
        return mostwords

mwf = MostWordsFound()
print("Most Words Found ::", mwf.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))

"""
Time Complexity:
- The method iterates through each sentence in the input list, which has length n.
- For each sentence, it performs a count of spaces, which takes O(m) time, where m is the length of the sentence.
- Assuming the total length of all sentences combined is M, the overall time complexity is O(M), since counting spaces in each sentence sums up to the total length of all sentences.

Space Complexity:
- The method uses a constant amount of extra space: variables mostwords and wordcount.
- No additional data structures proportional to input size are used.
- Therefore, the space complexity is O(1).

In summary:
Time complexity: O(M), where M is the total length of all sentences.
Space complexity: O(1).
"""