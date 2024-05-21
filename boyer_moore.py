def build_shift_table(pattern):
    table = {}
    m = len(pattern)
    for i in range(m - 1):
        table[pattern[i]] = m - 1 - i
    return table
def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    shifts = build_shift_table(pattern)
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j == -1:
            print("Подстрока найдена на позиции", i)
            i += 1
        else:
            shift = shifts.get(text[i + m - 1], m)
            i += shift
text = input("Введите текст: ")
pattern = input("Введите подстроку,которую хотите найти в тексте: ")
boyer_moore(text, pattern)