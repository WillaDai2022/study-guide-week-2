# Create your classes here
class Student:

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
    


class Question:

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        
        answer = input(self.question + " > ")

        return self.correct_answer == answer


class Exam:

    def __init__(self, name):
        self.questions = []
        self.name = name

    def add_question(self, question):
        self.questions.append(question)

    def administer(self):
        count = 0
        for question in self.questions:
            if question.ask_and_evaluate():
                count += 1
        
        return (count/len(self.questions))*100

class StudentExam:

    def __init__(self, student, exam):
        self.student = student
        self.exam = exam
        self.score = None

    def take_test(self):
        self.score = self.exam.administer()
        print(f"The score is {self.score:.2f} percent")

def example():
    exam = Exam("Midterm")

    q1 = Question(
        "What is the method for adding an element to a set?", 
        ".add()")

    exam.add_question(q1)

    q2 = Question(
    "What does pwd stand for?",
    "print working directory")

    exam.add_question(q2)

    q3 =  Question(
    'Python lists are mutable, iterable, and what?',
    'ordered')

    exam.add_question(q3)

    student = Student("Amy", "Kim", "1211 Succeed Rd")

    stu_exam = StudentExam(student, exam)

    stu_exam.take_test()

example()

class StudentQuiz(Exam):
    def administer(self):
        count = 0
        for question in self.questions:
            if question.ask_and_evaluate():
                count += 1
        
        if count >= len(self.questions):
            return 1
        else:
            return 0