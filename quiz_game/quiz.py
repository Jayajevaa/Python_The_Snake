from quiz_brain import QuizBrain
import os
import time
from data import question_data
from question_model import Question


question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
os.system('cls')
quiz = QuizBrain(question_bank)
print("Are you ready !!")


quiz.timer()

while quiz.still_has_question():

    quiz_question = quiz.next_question()

    time.sleep(2)
    if quiz.question_number < len(question_bank):
        print("Here is your next question")
    else:
        print("The quiz is over")
    time.sleep(1)
    os.system('cls')

os.system('cls')
print(f"Your final score is : {quiz.score}")
