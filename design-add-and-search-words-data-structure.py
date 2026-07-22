class Trie:
    def __init__(self, letter: str):
        self.children = {}
        self.letter = letter
        self.wordEnd = False

    def addWord(self, word: str) -> None:
        letterIndex = 0
        trie = self
        while letterIndex < len(word):
            letter = word[letterIndex]
            if letter in trie.children:
                trie = trie.children[letter]
            else:
                child = Trie(letter)
                trie.children[letter] = child
                trie = child
            letterIndex += 1
        trie.wordEnd = True

    def search(self, word: str, startIndex: int, depth: int) -> bool:
        letterIndex = startIndex
        trie = self
        while letterIndex < len(word):
            letter = word[letterIndex]
            if letter in trie.children:
                trie = trie.children[letter]
                depth += 1
            elif letter == ".":
                for key in trie.children.keys():
                    if trie.children[key].search(word, letterIndex + 1, depth + 1):
                        return True
            else:
                return False
            letterIndex += 1
        return letterIndex == depth and trie.wordEnd

class WordDictionary:

    def __init__(self):
        self.trie = Trie(None)
        self.trie.children = {}

    def addWord(self, word: str) -> None:
        self.trie.addWord(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word, 0, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
