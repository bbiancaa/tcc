class TrieNode:
    def __init__(self):
        self.children = {}  # Dicionário de filhos (letras) 
        self.is_end_of_word = False  # Marca o final de uma palavra

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Nó raiz da Trie

    def insert(self, word: str):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True  # Marca o final da palavra

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False  # Palavra não encontrada
            current = current.children[char]
        return current.is_end_of_word  # Verifica se é o final de uma palavra

    def starts_with(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False  # Prefixo não encontrado
            current = current.children[char]
        return True  # Prefixo encontrado

    def get_all_words_with_prefix(self, prefix: str) -> list:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []  # Se o prefixo não existir
            current = current.children[char]
        
        return self._get_words_from_node(current, prefix)
    
    def _get_words_from_node(self, node: TrieNode, prefix: str) -> list:
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        
        for char, child_node in node.children.items():
            words.extend(self._get_words_from_node(child_node, prefix + char))
        
        return words

# Exemplo de uso:
trie = Trie()

# Inserir palavras
palavras = ["cachorro", "cachorrinho", "gato", "gavião", "gafanhoto"]
for palavra in palavras:
    trie.insert(palavra)

# Buscar uma palavra específica
print(trie.search("cachorro"))  # True
print(trie.search("gato"))  # True
print(trie.search("gatoe"))  # False

# Buscar prefixo
print(trie.starts_with("ca"))  # True
print(trie.starts_with("gaf"))  # True
print(trie.starts_with("gavi"))  # True
print(trie.starts_with("go"))  # False

# Obter todas as palavras com um determinado prefixo
print(trie.get_all_words_with_prefix("ga"))  # ['gato', 'gavião', 'gafanhoto']
