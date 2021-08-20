from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_bank.append(Question(i['text'], i['answer']))
score = 0
quiz = QuizBrain(question_bank)
while quiz.question_number < len(question_bank):
    result = quiz.next_question()
    if result:
        score += 1
print(score)