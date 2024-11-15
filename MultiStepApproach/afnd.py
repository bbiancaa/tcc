class NFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def transition(self, state, symbol):
        return self.transition_function.get((state, symbol), set())

    def epsilon_closure(self, states):
        # Encontrar o fechamento epsilon de um conjunto de estados
        closure = set(states)
        to_process = list(states)
        while to_process:
            state = to_process.pop()
            if (state, '') in self.transition_function:
                for next_state in self.transition_function[(state, '')]:
                    if next_state not in closure:
                        closure.add(next_state)
                        to_process.append(next_state)
        return closure
class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

def nfa_to_dfa(nfa):
    start_state = frozenset(nfa.epsilon_closure([nfa.start_state]))
    dfa_states = {start_state}
    dfa_transitions = {}
    dfa_accept_states = set()
    state_mapping = {start_state: 'q0'}
    state_counter = 1

    unprocessed_states = [start_state]
    
    while unprocessed_states:
        current_state = unprocessed_states.pop()
        for symbol in nfa.alphabet:
            next_state = frozenset(nfa.epsilon_closure(
                [state for s in current_state for state in nfa.transition(s, symbol)]))
            if next_state:
                if next_state not in state_mapping:
                    state_mapping[next_state] = f'q{state_counter}'
                    dfa_states.add(next_state)
                    unprocessed_states.append(next_state)
                    state_counter += 1
                dfa_transitions[(state_mapping[current_state], symbol)] = state_mapping[next_state]
                if any(state in nfa.accept_states for state in next_state):
                    dfa_accept_states.add(state_mapping[next_state])

    return DFA(dfa_states, nfa.alphabet, dfa_transitions, state_mapping[start_state], dfa_accept_states)
# Definir o NFA para a expressão regular a*b
states = {'q0', 'q1', 'q2'}
alphabet = {'a', 'b'}
transition_function = {
    ('q0', 'a'): {'q0'},
    ('q0', 'b'): {'q1'},
    ('q1', 'b'): {'q2'}
}
start_state = 'q0'
accept_states = {'q2'}

nfa = NFA(states, alphabet, transition_function, start_state, accept_states)
dfa = nfa_to_dfa(nfa)

# Exibindo o DFA resultante
print("DFA States:", dfa.states)
print("DFA Transitions:", dfa.transition_function)
print("DFA Start State:", dfa.start_state)
print("DFA Accept States:", dfa.accept_states)
