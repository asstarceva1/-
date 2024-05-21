def rabin_karp(text, pattern):
    alphabet_size = 256
    prime = 101
    m = len(pattern)
    n = len(text)
    pattern_hash = 0
    text_hash = 0
    h = 1
    for i in range(m - 1):
        h = (h * alphabet_size) % prime
    for i in range(m):
        pattern_hash = (alphabet_size * pattern_hash + ord(pattern[i])) % prime
        text_hash = (alphabet_size * text_hash + ord(text[i])) % prime
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i + m]:
                print("Подстрока найдена на позиции", i)
        if i < n - m:
            text_hash = (alphabet_size * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime
text = input("Введите текст: ")
pattern = input("Введите подстроку,которую хотите найти в тексте: ")
rabin_karp(text, pattern)