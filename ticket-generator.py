import random
class Student:
    def __init__(self, fio):
        self.fio = fio
        self.questions = {}
    def add_question(self, topic, question_number):
        if topic in self.questions:
            self.questions[topic].append(question_number)
        else:
            self.questions[topic] = [question_number]
    def generate_ticket(self):
        ticket = f"{self.fio} ["
        for topic, question_numbers in self.questions.items():
            ticket += f"({topic}: "
            for question_number in question_numbers:
                ticket += f"{question_number}, "
            ticket = ticket[:-2]  # Удаляем лишнюю запятую и пробел
            ticket += "), "
        ticket = ticket[:-2]  # Удаляем последнюю запятую и пробел
        ticket += "]"
        return ticket
class Question:
    def __init__(self, topic, number, text):
        self.topic = topic
        self.number = number
        self.text = text
class Theme:
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, number, text):
        self.questions.append(Question(self.name, number, text))

    def get_random_question(self):
        if self.questions:
            return self.questions.pop(random.randint(0, len(self.questions) - 1))
def format_ticket(ticket):
    formatted_ticket = ""
    for line in ticket.split("\n"):
        formatted_ticket += "    " + line + "\n"
    return formatted_ticket
student_file_path = input("Введите путь к файлу с ФИО студентов: ")
question_file_path = input("Введите путь к файлу с вопросами и темами: ")
students = []
with open(student_file_path, "r") as file:
    for line in file:
        students.append(Student(line.strip()))
themes = []
current_theme = None
with open(question_file_path, "r") as file:
    for line in file:
        if line.startswith("Тема:"):
            current_theme = Theme(line.strip())
            themes.append(current_theme)
        elif current_theme:
            parts = line.strip().split(". ", 1)
            if len(parts) == 2:
                current_theme.add_question(parts[0], parts[1])
for student in students:
    for theme in themes:
        number_of_questions = int(input(f"Сколько вопросов из темы '{theme.name}' добавить в билет для студента {student.fio}: "))
        for _ in range(number_of_questions):
            random_question = theme.get_random_question()
            if random_question:
                student.add_question(random_question.topic, random_question.number)
tickets_file_path = "tickets.txt"
with open(tickets_file_path, "w") as file:
    for student in students:
        ticket = student.generate_ticket()
        file.write(format_ticket(ticket) + "\n\n")