class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        current_node = self.root
        # Objetivo: añadir cada letra de la palabra creando una estructura descendente (tipo raíz)
        for letter in word:
            if letter not in current_node:
                current_node[letter] = {}
            current_node = current_node[letter]
        current_node['*'] = {}
        print(self.root)

    def search_in_node(self, word, node):  # "a" "." "ma." ".ad" "b.."
        # Objetivo: encontrar la misma palabra en la estructura (puntos = comodín)
        current_node = node

        if len(word) == 0:
            return '*' in current_node
        # print('Current Node:', current_node)

        # Caso punto/comodín
        if word[0] == '.':
            for ch in current_node:
                if self.search_in_node(word[1:], current_node[ch]):
                    return True

        if word[0] in current_node:
            return self.search_in_node(word[1:], current_node[word[0]])
        else:
            return False

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.search_in_node(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()

obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
obj.addWord("badly")
obj.addWord("x")

print("pad ->", obj.search("pad"))
print("bad ->", obj.search("bad"))
print("math ->", obj.search("math"))

print("a ->", obj.search("a"))
print(". ->", obj.search("."))
print("ma. ->", obj.search("ma."))
print(".ad ->", obj.search(".ad"))
print("b.. ->", obj.search("b.."))

