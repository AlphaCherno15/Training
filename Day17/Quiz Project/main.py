from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
# start_line = 0
# for question in question_data:
#     new_question = Question(question_data[start_line]["text"], question_data[start_line]["answer"])
#     start_line += 1
#     question_bank.append(new_question.text)
#     question_bank.append(new_question.answer)

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz")
print(f'Your final score was: {quiz.score}/{quiz.question_number}')