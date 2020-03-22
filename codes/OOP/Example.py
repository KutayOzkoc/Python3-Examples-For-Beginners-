"""
    Question : Let's Create a quiz system
        program give some questions and user try to correct answer
        finally program will show result table
"""


class Question():
    def __init__(self, text, choice, answer):
        self.text = text
        self.choice = choice
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer


class Quiz():
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def diplayQuestion(self):
        a = 1
        question = self.getQuestion()
        print(f'Question {self.questionIndex + 1} : {question.text}')
        for i in question.choice:
            print(f'{a} -> '+i)
            a += 1
        answer = input('Answer : ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if(question.checkAnswer(answer)):
            self.score += 50
        self.questionIndex += 1

    def loadQuestion(self):
        if(len(self.questions) == self.questionIndex):
            self.showScore()
        else:
            self.diplayQuestion()

    def showScore(self):
        print(f'Your score is : {self.score} ')


q1 = Question('Whats the first programming language ? (50 points)',
              ['Pascal', 'Cobol', 'Plankalkül', 'Ada'], 'Plankalkül')
# You can create more than one question like this

q2 = Question('whats the first procedural language ? (50 points)',
              ['Pascal', 'Cobol', 'Plankalkül', 'Fortran'], 'Fortran')

question = [q1, q2]

quiz = Quiz(question)
question = quiz.getQuestion()
quiz.diplayQuestion()
print('The End')
