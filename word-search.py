class Solution:
    def check(self, board, word, row, col, letters):
        currLen = len(letters)
        if currLen == len(word):
            return True
        hasWord = False
        # Up
        if row > 0 and word[currLen] == board[row - 1][col] and (row - 1, col) not in letters:
            if currLen + 1 == len(word):
                return True
            hasWord = self.check(board, word, row - 1, col, letters + [(row - 1, col)])
        # Down
        if not hasWord and row < len(board) - 1 and word[currLen] == board[row + 1][col] and (row + 1, col) not in letters:
            if currLen + 1 == len(word):
                return True
            hasWord = self.check(board, word, row + 1, col, letters + [(row + 1, col)])
        # Left
        if not hasWord and col > 0 and word[currLen] == board[row][col - 1] and (row, col - 1) not in letters:
            if currLen + 1 == len(word):
                return True
            hasWord = self.check(board, word, row, col - 1, letters + [(row, col - 1)])
        # Right
        if not hasWord and col < len(board[0]) - 1 and word[currLen] == board[row][col + 1] and (row, col + 1) not in letters:
            if currLen + 1 == len(word):
                return True
            hasWord = self.check(board, word, row, col + 1, letters + [(row, col + 1)])

        return hasWord


    def exist(self, board: List[List[str]], word: str) -> bool:
        for wordRowStart in range(len(board)):
            for wordColStart in range(len(board[0])):
                if board[wordRowStart][wordColStart] == word[0] and self.check(board, word, wordRowStart, wordColStart, [(wordRowStart, wordColStart)]):
                    return True

        return False
