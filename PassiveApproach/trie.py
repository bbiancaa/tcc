class TrieNode:
    def __init__(self):
        self.children = {}  # Dicionário de filhos, onde chave é o caractere e valor é o nó filho.
        self.is_end_of_word = False  # Marca o final de uma palavra.


class Trie:
    def __init__(self):
        self.root = TrieNode()  # Raiz da Trie.

    def insert(self, word):
        node = self.root
        for char in word:
            # Se o caractere não está presente, cria-se um novo nó para esse caractere.
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True  # Marca o final da palavra.

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:  # Se algum caractere não for encontrado, a palavra não existe.
                return False
            node = node.children[char]
        return node.is_end_of_word  # Verifica se é o final de uma palavra completa.

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:  # Se algum caractere do prefixo não for encontrado.
                return False
            node = node.children[char]
        return True  # Prefixo encontrado.

# Testando a implementação com algumas palavras
trie = Trie()

# Inserindo palavras na Trie
palavras = ["apple", "app", "banana", "bat", "batman"]
for palavra in palavras:
    trie.insert(palavra)

# Buscando palavras na Trie
print(trie.search("apple"))  # True
print(trie.search("app"))  # True
print(trie.search("batman"))  # True
print(trie.search("bat"))  # True
print(trie.search("banana"))  # True
print(trie.search("ban"))  # False, 'ban' não é uma palavra completa na Trie

# Buscando por prefixos
print(trie.starts_with("app"))  # True
print(trie.starts_with("bat"))  # True
print(trie.starts_with("ban"))  # True
print(trie.starts_with("bana"))  # True
print(trie.starts_with("banx"))  # False

# Exemplo de inserção a partir de um arquivo
with open("dicionario.txt", "r") as file:
    for line in file:
        word = line.strip()
        trie.insert(word)
