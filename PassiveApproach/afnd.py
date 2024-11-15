class NFA:
    def __init__(self, states, alphabet, start_state, accept_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.start_state = start_state
        self.accept_states = accept_states
        self.transitions = transitions

def thompson_regex_to_nfa(regex):
    # Implementação simplificada do algoritmo de Thompson para construir um NFA
    # A ideia é construir um NFA para cada operação de concatenação, união e estrela
    # Dependendo da expressão regular, retornamos o NFA correspondente.
    pass
class DFA:
    def __init__(self, states, alphabet, start_state, accept_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.start_state = start_state
        self.accept_states = accept_states
        self.transitions = transitions

def nfa_to_dfa(nfa):
    # Um dicionário de estados do DFA, mapeando o conjunto de estados do NFA para um estado único no DFA
    dfa_states = {}
    dfa_start_state = frozenset([nfa.start_state])  # O estado inicial do DFA é o conjunto de estados iniciais do NFA
    dfa_accept_states = set()
    dfa_transitions = {}

    # Adiciona o estado inicial do DFA
    unmarked_states = [dfa_start_state]
    dfa_states[dfa_start_state] = len(dfa_states)  # Atribuindo um identificador único para cada conjunto de estados

    while unmarked_states:
        current_state = unmarked_states.pop()

        # Verificar se é um estado de aceitação no DFA
        if any(state in nfa.accept_states for state in current_state):
            dfa_accept_states.add(current_state)

        # Construir transições para os próximos estados
        for symbol in nfa.alphabet:
            next_state = set()
            for state in current_state:
                if state in nfa.transitions and symbol in nfa.transitions[state]:
                    next_state.update(nfa.transitions[state][symbol])
            if next_state:
                next_state = frozenset(next_state)  # Tornar o conjunto imutável
                if next_state not in dfa_states:
                    dfa_states[next_state] = len(dfa_states)
                    unmarked_states.append(next_state)
                dfa_transitions[current_state, symbol] = next_state

    return DFA(dfa_states, nfa.alphabet, dfa_start_state, dfa_accept_states, dfa_transitions)
# Exemplo: Expressão regular (ab|cd)*

regex = "(ab|cd)*"

# 1. Construa o NFA a partir da expressão regular
nfa = thompson_regex_to_nfa(regex)

# 2. Converta o NFA para um DFA
dfa = nfa_to_dfa(nfa)

# 3. Exiba os resultados (por exemplo, transições e estados finais)
print("DFA States:", dfa.states)
print("DFA Start State:", dfa.start_state)
print("DFA Accept States:", dfa.accept_states)
print("DFA Transitions:", dfa.transitions)
