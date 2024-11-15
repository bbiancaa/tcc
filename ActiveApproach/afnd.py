import re
from collections import defaultdict

# Definindo a estrutura para um estado
class State:
    def __init__(self, name):
        self.name = name
        self.transitions = defaultdict(set)  # Transições do estado (simbolos -> estados)

# Função para construir o NFA usando o algoritmo de Thompson
def thompson_regex_to_nfa(regex):
    stack = []
    
    # Para cada caractere da expressão regular
    for char in regex:
        if char == '*':
            nfa2 = stack.pop()
            start_state = State('start')
            end_state = State('end')
            start_state.transitions[None].add(nfa2.start)
            nfa2.end.transitions[None].add(end_state)
            start_state.transitions[None].add(end_state)
            nfa2.end.transitions[None].add(nfa2.start)
            stack.append((start_state, end_state))
        elif char == '|':  # Operador OR
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            start_state = State('start')
            end_state = State('end')
            start_state.transitions[None].add(nfa1.start)
            start_state.transitions[None].add(nfa2.start)
            nfa1.end.transitions[None].add(end_state)
            nfa2.end.transitions[None].add(end_state)
            stack.append((start_state, end_state))
        elif char == '.':  # Operador de concatenação
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            nfa1.end.transitions[None].add(nfa2.start)
            stack.append((nfa1.start, nfa2.end))
        else:  # Alfabeto de entrada (um caractere)
            start_state = State('start')
            end_state = State('end')
            start_state.transitions[char].add(end_state)
            stack.append((start_state, end_state))
    
    return stack.pop()

# Função para converter um NFA para um DFA (algoritmo de subconjuntos)
def nfa_to_dfa(nfa):
    dfa_states = []
    dfa_transitions = {}
    start_state = frozenset([nfa[0][0]])  # Estado inicial do DFA, conjunto de estados do NFA
    dfa_states.append(start_state)
    unprocessed = [start_state]
    state_map = {start_state: 'q0'}
    
    while unprocessed:
        current_state = unprocessed.pop()
        for symbol in set(char for state in current_state for char in state.transitions.keys()):
            next_state = frozenset(
                next_state for state in current_state for next_state in state.transitions.get(symbol, [])
            )
            if next_state:
                if next_state not in dfa_states:
                    dfa_states.append(next_state)
                    unprocessed.append(next_state)
                dfa_transitions[(state_map[current_state], symbol)] = state_map.get(next_state, f'q{len(state_map)}')
                state_map[next_state] = state_map.get(next_state, f'q{len(state_map)}')
    
    return dfa_states, dfa_transitions

# Função para testar a expressão regular
def test_dfa(dfa, dfa_transitions, string):
    state = 'q0'
    for symbol in string:
        state = dfa_transitions.get((state, symbol))
        if state is None:
            return False
    return True

# Exemplo de uso
regex = "ab*"
nfa = thompson_regex_to_nfa(regex)
dfa_states, dfa_transitions = nfa_to_dfa(nfa)

# Exibir a conversão
print("Estados do DFA:", dfa_states)
print("Transições do DFA:", dfa_transitions)

# Testando o DFA
input_string = "abb"
print("Aceita a string '{}': {}".format(input_string, test_dfa(dfa_states, dfa_transitions, input_string)))
