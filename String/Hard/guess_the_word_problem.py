class Solution(object):
    def findSecretWord(self, words, master):
        for _ in range(10):
            # Count matches for each word with all others
            count = {}
            for word in words:
                count[word] = [0] * 7
                for w in words:
                    if word != w:
                        match = self.checkMatch(word, w)
                        count[word][match] += 1
            # Choose the word that minimizes the largest group
            guess_word = min(words, key=lambda w: max(count[w]))
            matches = master.guess(guess_word)
            if matches == 6:
                return
            words = [w for w in words if self.checkMatch(w, guess_word) == matches]

    def checkMatch(self, word1, word2):
        return sum(a == b for a, b in zip(word1, word2))


class Master:
    def __init__(self, secret):
        self.secret = secret
        self.attempts = 0

    def guess(self, word):
        self.attempts += 1
        return sum(a == b for a, b in zip(word, self.secret))


sol = Solution()
master = Master("acckzz")
sol.findSecretWord(words=["acckzz", "ccbazz", "eiowzz", "abcczz"], master=master)


"""
Solution 1:: Not working correctly in leetcode.

import random
class Solution(object):
    def findSecretWord(self, words, master):
        guesses = 0
        lettersGuessed = 0
        numguesses = 30
        while guesses < numguesses and lettersGuessed < 6 and words:
            randomword = random.choice(words)
            lettersGuessed = master.guess(randomword)
            candidates = []
            for word in words:
                if lettersGuessed == self.checkMatch(word, randomword):
                    candidates.append(word)
            words = candidates
            guesses += 1
        return None

    def checkMatch(self, word, randomword):
        lettersMatched = 0
        for i in range(6):
            if word[i] == randomword[i]:
                lettersMatched += 1
        return lettersMatched
"""