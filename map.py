class Map:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]
    def hash_function(self, key):
        return hash(key) % self.size
    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
    def get(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for existing_key, value in bucket:
            if existing_key == key:
                return value
        raise KeyError(key)
    def contains(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]

        for existing_key, _ in bucket:
            if existing_key == key:
                return True
        return False
    def remove(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                return
        raise KeyError(key)
my_map = Map()
while True:
    command = input("Введите команду (insert, get, contains, remove, exit): ").strip().lower()
    if command == "insert":
        key = input("Введите ключ: ")
        value = input("Введите значение: ")
        my_map.insert(key, value)
        print("Элемент добавлен в карту.")
    elif command == "get":
        key = input("Введите ключ: ")
        try:
            print("Значение:", my_map.get(key))
        except KeyError:
            print("Ключ не найден.")
    elif command == "contains":
        key = input("Введите ключ: ")
        if my_map.contains(key):
            print("Ключ найден.")
        else:
            print("Ключ не найден.")
    elif command == "remove":
        key = input("Введите ключ: ")
        try:
            my_map.remove(key)
            print("Элемент удален.")
        except KeyError:
            print("Ключ не найден.")
    elif command == "exit":
        print("Выход из программы.")
        break
    else:
        print("Неверная команда. Пожалуйста, введите одну из указанных команд.")