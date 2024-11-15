class TrieNode:
    def __init__(self):
        # Cada nó pode ter 26 filhos (um para cada letra do alfabeto)
        self.children = {}
        self.is_end_of_word = False  # Marca se é o final de uma palavra

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        # Método para inserir uma palavra na Trie
        node = self.root
        for char in word:
            # Para cada caractere na palavra, insira ou vá para o próximo nó
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True  # Marca o final da palavra

    def search(self, word: str) -> bool:
        # Método para buscar uma palavra na Trie
        node = self.root
        for char in word:
            if char not in node.children:
                return False  # Se algum caractere não for encontrado, a palavra não existe
            node = node.children[char]
        return node.is_end_of_word  # Verifica se é o final de uma palavra válida

    def starts_with(self, prefix: str) -> bool:
        # Método para verificar se existe alguma palavra que começa com o prefixo
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False  # Se algum caractere não for encontrado, não há palavras com esse prefixo
            node = node.children[char]
        return True  # Se percorreu todo o prefixo, significa que existe pelo menos uma palavra com ele
# Criando a Trie
trie = Trie()

# Inserindo algumas palavras
words = ["cachorro", "gato", "gavião", "girafa", "cavalo"]
for word in words:
    trie.insert(word)

# Buscando palavras
print(trie.search("cachorro"))  # True
print(trie.search("gato"))  # True
print(trie.search("gatoa"))  # False

# Verificando prefixos
print(trie.starts_with("ga"))  # True
print(trie.starts_with("ca"))  # True
print(trie.starts_with("gu"))  # False

# Supondo que você tenha um arquivo com 1 milhão de palavras, como 'dictionary.txt'
# Cada linha contém uma palavra

trie = Trie()

# Carregar palavras de um arquivo
with open("dictionary.txt", "r") as file:
    for word in file:
        trie.insert(word.strip())  # Remover a quebra de linha antes de inserir

# Buscar uma palavra específica
print(trie.search("programação"))
