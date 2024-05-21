def build_transition_table(pattern):
    m = len(pattern)
    alphabet = set(pattern)
    table = [{char: 0 for char in alphabet} for _ in range(m + 1)]
    for state in range(m + 1):
        for char in alphabet:
            next_state = min(m, state + 1)
            while next_state > 0 and pattern[:next_state] != pattern[state - next_state + 1:state] + char:
                next_state -= 1
            table[state][char] = next_state
    return table
def finite_automaton(text, pattern):
    m = len(pattern)
    n = len(text)
    transitions = build_transition_table(pattern)
    state = 0
    for i in range(n):
        state = transitions[state].get(text[i], 0)
        if state == m:
            print("Подстрока найдена на позиции", i - m + 1)
text = input("Введите текст: ")
pattern = input("Введите подстроку,которую хотите найти в тексте: ")
finite_automaton(text, pattern)