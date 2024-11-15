class TrieNode:
    def __init__(self):
        self.children = {}  # Dicionário de filhos
        self.is_end_of_word = False  # Marca se é o fim de uma palavra

class Trie:
    def __init__(self):
        self.root = TrieNode()  # A raiz da árvore

    def insert(self, word):
        node = self.root
        for char in word:
            # Se o caractere não existir, cria um novo nó
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True  # Marca o fim da palavra

    def search(self, word):
        node = self.root
        for char in word:
            # Se o caractere não estiver na árvore, a palavra não existe
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word  # Verifica se é o fim de uma palavra

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            # Se o prefixo não existir, retorna False
            if char not in node.children:
                return False
            node = node.children[char]
        return True  # O prefixo existe

# Exemplo de uso
trie = Trie()
words = ["cachorro", "cachorrinho", "gato", "gatozinho", "passaro"]

for word in words:
    trie.insert(word)

# Testando as buscas
print(trie.search("cachorro"))  # True
print(trie.search("gato"))      # True
print(trie.search("gatinho"))   # False
print(trie.starts_with("gato")) # True

import random
import time

# Gerando um dicionário com 1 milhão de palavras fictícias
def generate_large_dict(num_words):
    words = set()
    while len(words) < num_words:
        word = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))  # Palavras de 10 caracteres
        words.add(word)
    return list(words)

# Criando a trie e inserindo 1 milhão de palavras
large_dict = generate_large_dict(1000000)

trie_large = Trie()

# Medindo o tempo de inserção
start_time = time.time()
for word in large_dict:
    trie_large.insert(word)
insert_time = time.time() - start_time

# Medindo o tempo de busca
search_word = random.choice(large_dict)  # Palavra que sabemos que existe
start_time = time.time()
result = trie_large.search(search_word)
search_time = time.time() - start_time

print(f"Tempo de inserção para 1 milhão de palavras: {insert_time:.4f} segundos")
print(f"Tempo de busca para a palavra '{search_word}': {search_time:.6f} segundos")
