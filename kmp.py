def build_prefix_table(pattern):
    m = len(pattern)
    prefix = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix[i] = j
    return prefix
def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    prefix_table = build_prefix_table(pattern)
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = prefix_table[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            print("Подстрока найдена на позиции", i - m + 1)
            j = prefix_table[j - 1]
text = input("Введите текст: ")
pattern = input("Введите подстроку,которую хотите найти в тексте: ")
kmp(text, pattern)