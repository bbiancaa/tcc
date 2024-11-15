import re

class NFA:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transitions = {}
        self.start_state = None
        self.accept_states = set()

    def add_state(self, state):
        self.states.add(state)
        self.transitions[state] = {}

    def set_start_state(self, state):
        self.start_state = state

    def add_accept_state(self, state):
        self.accept_states.add(state)

    def add_transition(self, from_state, symbol, to_state):
        if symbol not in self.transitions[from_state]:
            self.transitions[from_state][symbol] = set()
        self.transitions[from_state][symbol].add(to_state)

    def __repr__(self):
        return f'NFA(states={self.states}, transitions={self.transitions}, start_state={self.start_state}, accept_states={self.accept_states})'


def thompson(regex):
    nfa_stack = []
    for char in regex:
        if char == '*':
            nfa = nfa_stack.pop()
            start_state = f's{len(nfa_stack)}'
            accept_state = f's{len(nfa_stack)+1}'
            nfa.add_state(start_state)
            nfa.add_state(accept_state)
            nfa.set_start_state(start_state)
            nfa.add_accept_state(accept_state)
            nfa.add_transition(start_state, 'ε', nfa.start_state)
            nfa.add_transition(nfa.accept_states.pop(), 'ε', accept_state)
            nfa.add_transition(nfa.accept_states.pop(), 'ε', start_state)
            nfa.add_transition(start_state, 'ε', accept_state)
            nfa_stack.append(nfa)
        elif char == '|':
            nfa2 = nfa_stack.pop()
            nfa1 = nfa_stack.pop()
            start_state = f's{len(nfa_stack)}'
            accept_state = f's{len(nfa_stack)+1}'
            nfa1.add_state(start_state)
            nfa2.add_state(start_state)
            nfa1.add_state(accept_state)
            nfa2.add_state(accept_state)
            nfa1.add_transition(start_state, 'ε', nfa1.start_state)
            nfa2.add_transition(start_state, 'ε', nfa2.start_state)
            nfa1.add_transition(nfa1.accept_states.pop(), 'ε', accept_state)
            nfa2.add_transition(nfa2.accept_states.pop(), 'ε', accept_state)
            nfa_stack.append(nfa1)
        elif char == '.':
            nfa2 = nfa_stack.pop()
            nfa1 = nfa_stack.pop()
            nfa1.add_state(f's{len(nfa1.states)}')
            nfa2.add_state(f's{len(nfa2.states)}')
            nfa1.add_state(f's{len(nfa1.states) + 1}')
            nfa1.set_start_state(nfa2.start_state)
            nfa1.add_accept_state(f's{len(nfa1.states)}')
            nfa2.add_transition(nfa2.start_state, 'ε', nfa2.start_state)
            nfa_stack.append(nfa1)

    return nfa_stack[0]


# exemplo de uso
regex = "a|b"
nfa = thompson(regex)
print(nfa)
class DFA:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transitions = {}
        self.start_state = None
        self.accept_states = set()

    def add_state(self, state):
        self.states.add(state)

    def set_start_state(self, state):
        self.start_state = state

    def add_accept_state(self, state):
        self.accept_states.add(state)

    def add_transition(self, from_state, symbol, to_state):
        if from_state not in self.transitions:
            self.transitions[from_state] = {}
        self.transitions[from_state][symbol] = to_state

    def __repr__(self):
        return f'DFA(states={self.states}, transitions={self.transitions}, start_state={self.start_state}, accept_states={self.accept_states})'


def nfa_to_dfa(nfa):
    dfa = DFA()
    initial_state = frozenset([nfa.start_state])
    dfa.set_start_state(initial_state)
    dfa.add_state(initial_state)

    unprocessed_states = [initial_state]
    while unprocessed_states:
        current = unprocessed_states.pop()
        for symbol in nfa.alphabet:
            next_state = frozenset(
                state for s in current for state in nfa.transitions[s].get(symbol, [])
            )
            if next_state:
                dfa.add_state(next_state)
                dfa.add_transition(current, symbol, next_state)
                if next_state not in unprocessed_states:
                    unprocessed_states.append(next_state)
                if any(state in nfa.accept_states for state in next_state):
                    dfa.add_accept_state(next_state)

    return dfa

# exemplo de uso para converter o NFA gerado:
dfa = nfa_to_dfa(nfa)
print(dfa)
